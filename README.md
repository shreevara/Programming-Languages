SHREEVARA ANDILA <br>
sandila1@binghamton.edu 
<hr>

<h3> Project1 </h3>

Programming Language Used: Python <br>
<h3> Grammar: </h3>
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

<h4> How to run the code: </h4>

$ echo '<i>provide input here</i>' | ./desig-inits.sh | json_pp
