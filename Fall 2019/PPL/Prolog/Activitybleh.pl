is_true(Question) :- format('~w?~n', [Question]), read(yes).

animal(dog) :- is_true('has fur'), is_true('says woof').
animal(cat) :- is_true('has fur'), is_true('says meow').
animal(duck) :- is_true('has feathers'), is_true('says quack').
animal(saproling) :- is_true('has cuticles'), is_true('says, "father, no..."').







