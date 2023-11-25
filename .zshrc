setopt completealiases

alias dotfiles="git --git-dir=$HOME/dotfiles --work-tree=$HOME"
alias dc="docker compose"
alias tf=terraform
alias vim=nvim
alias hx=helix
alias ycs3="aws s3 --endpoint-url=https://storage.yandexcloud.net"

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi

# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

# Updates PATH for Yandex Cloud CLI.
if [[ -e $HOME/yandex-cloud/path.bash.inc ]]; then
    source $HOME/yandex-cloud/path.bash.inc
fi

# Enables shell command completion for yc.
if [[ -e $HOME/yandex-cloud/completion.zsh.inc ]]; then
    source $HOME/yandex-cloud/completion.zsh.inc
fi

export PATH=~/.local/share/gem/ruby/3.0.0/bin:$PATH
export PATH=~/.cargo/bin:$PATH
export PATH=/opt/flutter/bin:$PATH

export WORKON_HOME=$HOME/.virtualenvwrapper
source $HOME/.local/bin/virtualenvwrapper.sh

export EDITOR=/usr/bin/nvim
export LD_LIBRARY_PATH=/usr/lib
export RUSTC_WRAPPER=sccache

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

source $HOME/.config/broot/launcher/bash/br

eval "$(fnm env --use-on-cd)"
eval "$(zoxide init zsh)"

