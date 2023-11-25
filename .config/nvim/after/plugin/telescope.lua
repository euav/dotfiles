local builtin = require('telescope.builtin')

vim.keymap.set('n', '<C-p>', builtin.git_files, {})
vim.keymap.set('n', '<leader>se', builtin.find_files, {})
vim.keymap.set('n', '<leader>sg', builtin.live_grep, {})
vim.keymap.set('n', '<leader>st', builtin.buffers, {})
vim.keymap.set('n', '<leader>sh', builtin.help_tags, {})
