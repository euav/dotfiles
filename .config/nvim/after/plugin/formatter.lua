local util = require "formatter.util"
local filetypes = require "formatter.filetypes"

function isort()
  return {
    exe = "isort",
    args = { "-q", util.escape_path(util.get_current_buffer_file_path()) },
    stdin = false
  }
end

function black()
  return {
    exe = "black",
    args = { "-q", util.escape_path(util.get_current_buffer_file_path()) },
    stdin = false
  }
end

require("formatter").setup {
  logging = true,
  log_level = vim.log.levels.INFO,

  -- All formatter configurations are opt-in
  filetype = {
    python = { isort, black },

    lua = {
      filetypes.lua.stylua,

      -- You can also define your own configuration
      function()
        -- Supports conditional formatting
        if util.get_current_buffer_file_name() == "special.lua" then
          return nil
        end

        -- Full specification of configurations is down below and in Vim help
        -- files
        return {
          exe = "stylua",
          args = {
            "--search-parent-directories",
            "--stdin-filepath",
            util.escape_path(util.get_current_buffer_file_path()),
            "--",
            "-",
          },
          stdin = true,
        }
      end
    }
  }
}
