# Ocaml

## Run code

```
ocaml filename.ml
```

Tested on version 4.05.0

## Vim supports

Install

```
opam install merlin ocp-indent
```

Append to vimrc.

```vim
setlocal rtp+=~/.opam/default/share/merlin/vim
setlocal rtp^="~/.opam/default/share/ocp-indent/vim"
```


### OCP-indent
`OCP-` stands for [Ocaml Pro](https://github.com/OCamlPro).
helps formatting.


### Merlin
Helps autocomplete.

## Better interactive shell

```
opam install utop
```

Then run `utop`
