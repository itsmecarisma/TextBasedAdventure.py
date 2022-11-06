// This is a
sub


class Cat which inherits all the properties of Pet class


public


class Cat extends Pet {
// instance variables for Cat


class is defined here


public
int
catSpaceNbr;

public
Cat()
{} // No
argument
constructor

public
Cat(int
catSpaceNbr) { // parameterized
constructor
this.catSpaceNbr = catSpaceNbr;
}

public
int
getCatSpaceNbr()
{ // accessor
method
for catSpaceNbr
    return catSpaceNbr;
}

public
void
setCatSpaceNbr(int
catSpaceNbr)  { // mutator
method
for catSpaceNbr
    this.catSpaceNbr = catSpaceNbr;
}
}