scalar_mult(_,[],[]).
scalar_mult(X,[H|T1],[V|T2]) :- scalar_mult(X,T1,T2), V is 3*H.
