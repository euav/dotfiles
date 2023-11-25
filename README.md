My dotfiles managed as *bare* git repository. You can read more [here](https://www.atlassian.com/git/tutorials/dotfiles).

### Installation

Clone the repo
```sh
git clone --bare https://github.com/euav/dotfiles.git $HOME/.dotfiles
```

Checkout at home
```sh
alias dotfiles="git --git-dir=$HOME/.dotfiles --work-tree=$HOME"
dotfiles checkout
```

### Usage

```sh
dotfiles add .some_config_file
dotfiles commit -m "Add .some_config_file"
dotfiles push
```
