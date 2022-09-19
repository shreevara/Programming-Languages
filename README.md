<<<<<<< prj1
SHREEVARA ANDILA <br>
sandila1@binghamton.edu 
<hr>

<h3> Project1 </h3>

Programming Language Used: Python <br>
<h3> Grammar: </h3><br>
val<br>
  : INT<br>
  | '{' initializers '}'<br>
  ;<br>
 initializers<br>
  : initializer ( ',' initializer )* ','? //optional comma after last init<br>
  | //empty<br>
  ;<br>
initializer<br>
  : '[' INT '] '=' val              //simple designated initializer<br>
  | '[' INT '...' INT ']' '=' val   //range designated initializer<br><br>
  | val                             //positional initializer<br>
  ;<br>
<br>
<h4> How to run the code: </h4><br>
$ echo '<input>' | ./desig-inits.sh | json_pp<br>
=======
<h3> Project1 final submitted code can be found in prj1 branch </h3>
>>>>>>> main
