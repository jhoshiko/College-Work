/* Gerom Pagaduan
 * Joshua Hoshiko
 * CS 3210 - Mota
 * Programming Assignment 3
 * 24 November, 2019
*/

:- dynamic fact/1.
:- dynamic nonfact/1.


is_true(Question):-
(
      fact(Question) ->
      true;
      nonfact(Question) -> false;
      (
      format('~w~n', [Question]), Answer = read(yes),
       Answer -> assert(fact(Question)); assert(nonfact(Question)), false
      )
).


food(bacon_and_eggs) :- is_true('is breakfast'), is_true('has eggs'), is_true('has meat').
food(omelette) :- is_true('is breakfast'), is_true('has eggs'), is_true('has meat'), is_true('is folded').
food(waffle) :- is_true('is breakfast'), is_true('is baked'), is_true('has patterns').
food(bagel) :- is_true('is breakfast'), is_true('is baked'), is_true('is held').
food(pancakes) :- is_true('is breakfast'), is_true('is fried').

food(pizza) :- is_true('is lunch'), is_true('has cheese').
food(buffalo_wings) :- is_true('is lunch'), is_true('has meat'), is_true('has buffalo sauce').
food(burrito) :- is_true('is lunch'), is_true('has meat'), is_true('has wrap').
food(hamburger) :- is_true('is lunch'), is_true('has meat').
food(salad) :- is_true('is lunch'), is_true('has leaves').

food(fried_chicken) :- is_true('is dinner'), is_true('has meat'), is_true('is poultry'), is_true('is fried').
food(roasted_turkey) :- is_true('is dinner'), is_true('has meat'), is_true('is poultry').
food(steak) :- is_true('is dinner'), is_true('has meat').
food(pho) :- is_true('is dinner'), is_true('has noodles'), is_true('is soup').
food(spaghetti) :- is_true('is dinner'), is_true('has noodles').


begin :- write('Welcome to the ES about cuisines!
I am going to ask questions about animal features.
Please answer yes. or no.
Ready?  '),
      read(Answer),
      nl,
      ((Answer == yes) -> assertz(yes(Answer)), bridge;
       (Answer == no) -> assertz(no(Answer)), write('Goodbye, friend. Type in "begin" to see me again.') ;
        write('\nInvalid Input.\n'), fail).


bridge :- retractall(fact(_)), retractall(nonfact(_)), food(A), write(A),
          nl,
          write('Is "'), write(A), write('" the correct answer?'),
          nl,
          read(Answer),
         ((Answer == yes) -> assertz(yes(Answer)), write('\nOh, thank the heavens.\n'),
          nl,
          write('To try again, type in "begin".');
         (Answer == no) -> assertz(no(Answer)), write('\nTHE IGNORANCE OF MY DEVELOPER CANNOT BE FORGIVEN.\n'),
          nl,
          write('To try again, type in "begin".');
          write('\nInvalid input, please answer with yes or no.\n'), fail).











