#!/usr/bin/env racket

;comment out following line to run in repl
#lang racket
(require rackunit)

;to trace function fn, add (trace fn) after fn's definition
(require racket/trace)  

;;; Some of the exercises below refer to employees.
;;; An employee is represented by a 4-tuple (name age department salary)

;;test data for employees
(define EMPLOYEES
  '((tom 33 cs 85000.00)
    (joan 23 ece 110000.00)
    (bill 29 cs 69500.00)
    (john 28 me 58200.00)
    (sue 19 cs 22000.00)
    ))

;; #1: 15-points
;;return list of employees having department dept
;;must be implemented recursively
;; Hint: use equal? to check for department equality
(define dept-employees
  (lambda (dept employees)
    (if (equal? employees null)
      '()
      (
      if (equal? (list-ref (car employees) 2) dept)
      (cons (car employees) (dept-employees dept (cdr employees)))
      (dept-employees dept (cdr employees))
      )
    )
))

(check-equal? (dept-employees 'ece EMPLOYEES) '((joan 23 ece 110000.00)))
(check-equal? (dept-employees 'cs EMPLOYEES)
	      '((tom 33 cs 85000.00)
 		(bill 29 cs 69500.00)
		(sue 19 cs 22000.00)
		))
(check-equal? (dept-employees 'ce EMPLOYEES) '())

;; #2: 5-points
;;return list of names of employees belonging to department dept
;;must be implemented recursively
;;Hint: almost the same as the previous exercise
(define dept-employees-names
  (lambda (dept employees)
    (if (equal? employees null)
      '()
      (
      if (equal? (list-ref (car employees) 2) dept)
      (cons (list-ref (car employees) 0) (dept-employees-names dept (cdr employees)))
      (dept-employees-names dept (cdr employees))
      )
    )
))

(check-equal? (dept-employees-names 'ece EMPLOYEES) '(joan))
(check-equal? (dept-employees-names 'cs EMPLOYEES) '(tom bill sue))
(check-equal? (dept-employees-names 'ce EMPLOYEES) '())

;; #3: 15-points
;;Given list indexes containing 0-based indexes and a list possibly
;;containing lists nested to an abitrary depth, return the element
;;in list indexed successively by indexes. Return 'nil if there is
;;no such element.
;;Hint: use list-ref
(define list-access
  (lambda (indexes l)
  (if (equal? indexes '())
    l
    (if (equal? (cdr indexes) null )
    (if (> (car indexes) (- (length l) 1))
      'nil
      (list-ref l (car indexes))
    )
    (list-access  (cdr indexes) (list-ref l (car indexes) ) ) 
    )
  )
  )
)

(check-equal? (list-access '(1) '(a b c)) 'b)
(check-equal? (list-access '(2) '(a b (c))) '(c))
(check-equal? (list-access '(2 0) '(a b (c))) 'c)
(check-equal? (list-access '(3) '(a b (c))) 'nil)
(check-equal? (list-access '(2 1) '(a b (c))) 'nil)
(check-equal? (list-access '() '((1 2 3) (4 (5 6 (8)))) )
      '((1 2 3) (4 (5 6 (8)))))
(check-equal? (list-access '(1) '((1 2 3) (4 (5 6 (8)))) )
	      '(4 (5 6 (8))))
(check-equal? (list-access '( 1 1 2) '((1 2 3) (4 (5 6 (8)))) )
 	      '(8))
(check-equal? (list-access '( 1 1 2 0) '((1 2 3) (4 (5 6 (8)))) )
	      '8)
(check-equal? (list-access '(0 1) '((1))) 'nil)

;; #4: 15-points
;;return sum of salaries for all employees
;;must be tail-recursive
;;Hint: use a nested auxiliary function with an accumulating parameter
(define (employees-salary-sum employees)
  (letrec ([aux-fact
	 (lambda (acc employees)
	   (if (pair? employees) 
	       (aux-fact (+ acc (cadddr (car employees))) (cdr employees))
	       acc)
	 )])
    (aux-fact 0 employees)
  )
)

(check-equal? (employees-salary-sum EMPLOYEES) 344700.00)
(check-equal? (employees-salary-sum '()) 0)

;; #5: 15-points
;;return list of pairs giving name and salary of employees belonging to
;;department dept
;;cannot use recursion
;;Hint: use filter and map from the standard Racket library
;;(google "racket filter", "racket map")
(define dept-employees-names-salaries 
  (lambda (dept employees)
  (map (lambda (l) 
      (append (list(car l)) (list(cadddr l)) )
      )
  (filter (lambda (l) (equal? dept (caddr l) )) employees) )
  )
)

(check-equal? (dept-employees-names-salaries 'ece EMPLOYEES) '((joan 110000.00)))
(check-equal? (dept-employees-names-salaries 'cs EMPLOYEES)
	      '((tom 85000.00)
		(bill 69500.00)
 		(sue 22000.00)
 		))
(check-equal? (dept-employees-names-salaries 'ce EMPLOYEES) '())

;; #6: 15-points
;;return average salary of all employees; 0 if employees empty
;;cannot use recursion
;;Hint: use foldl from the standard Racket library
;;(google "racket foldl").
(define employees-average-salary 
  (lambda (employees)
    (/ (foldl (lambda (v l) (+ l (cadddr v) )) 0 employees ) (length EMPLOYEES))
  )
)

(check-equal? (employees-average-salary EMPLOYEES) (/ 344700.00 5))
(check-equal? (employees-average-salary '()) 0)

;; #7: 20-points
;; given an integer or list of nested lists containing integers,
;; return a string containing its JSON representation without any
;; whitespace
;; Hints: use (number->string n) to convert integer n to a string.
;;        use (string-append str1 str2 ...) to append str1 str2 ...
;;        use (string-join str-list sep) to join strings in str-list using sep
;; also see toJson() methods in java-no-deps Parser.java in prj1-sol


;; for checking base conditions and joining strings with string-join
(define int-list-json
  (lambda (int-list)
    (cond
    [(equal? int-list null) "[]"]
    [(integer? int-list) (number->string int-list)]
    [else (string-join (first int-list)  ",")]
    )
  )
)
;;calling all other functions
(define first
  (lambda (eq3)
    (define eq4 (final eq3))
    (append (list(string-append (car eq4) (cadr eq4))) (cddr eq4))
  )
)
;;adding starting bracket
(define final
  (lambda (jsonl)
    (define eq1 (flatten jsonl))
    (define second (lapp eq1))
    (define third (lapp second))
    (append (list "[") (lapp third))
  )
)
;;string-append "]" brackets with previous values
(define lapp 
  (lambda (ll)
    (cond 
      [(equal? ll null) ll]
      [(equal? (cdr ll) null) ll]
      [(equal? (cadr ll) "]") (append (list(string-append (car ll) (cadr ll))) (lapp (cddr ll))  ) ]
      [(equal? (cadr ll) "]]") (append (list(string-append (car ll) (cadr ll))) (lapp (cddr ll))  ) ]
      [else (append (list(car ll)) (lapp (cdr ll))) ]
  
    )
  )
)
;;converting number to string.
(define (flatten l)
  (cond 
        [(equal? l null) (list "]")]
        [(not (list? l)) (list (number->string l))]
        [else 
        (if (list? (car l))
        (append (list (string-append "[" (car (flatten (car l))) )) (flatten (cdar l))  (flatten (cdr l)))
        (append (flatten (car l)) (flatten (cdr l)) )
        )]
  )
  
)
      

(check-equal? (int-list-json '(1 2 3)) "[1,2,3]")
(check-equal? (int-list-json '(1 (2 (4 5) 6))) "[1,[2,[4,5],6]]")
(check-equal? (int-list-json '()) "[]")
(check-equal? (int-list-json 42) "42")
	 