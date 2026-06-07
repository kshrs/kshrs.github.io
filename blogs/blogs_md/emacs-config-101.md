# Emacs config 101: from zero to modal editing

date: 2026-01-15

I've been a `vim` user for years, but the siren call of Emacs' extensibility (`M-x butterfly`) finally got me.  
Here's how I built my **minimal, evil-mode based configuration** — no bloat, just results.

## Why Emacs?

- **One environment** for code, email, org-mode, and even terminal.
- **Elisp** is weird but powerful.
- Modal editing? `evil-mode` gives you Vim keys inside Emacs. Best of both worlds.

## My base init.el

Start with this skeleton:

```elisp
;; init.el – minimal literate config
(require 'package)
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("gnu" . "https://elpa.gnu.org/packages/")))
(package-initialize)

;; Install use-package if missing
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

;; evil-mode (modal editing)
(use-package evil
  :ensure t
  :config
  (evil-mode 1))

;; theme – dark, clean
(use-package doom-themes
  :ensure t
  :config
  (load-theme 'doom-one t))

```
