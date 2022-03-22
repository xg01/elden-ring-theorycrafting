{ 
  channel         ? import <nixos>          { config.allowUnfree = true; }, 
  unstableChannel ? import <nixos-unstable> { config.allowUnfree = true; },
  nixpkgs         ? import <nixpkgs>        { config.allowUnfree = true; },
  python          ? channel.python39,
  gcc             ? channel.gcc11Stdenv.mkDerivation, 
  shell-env       ? gcc
}:

let 
  stable-pkgs = with channel; {
    python-devchain = python.withPackages (p: with p; [
      numpy pandas scikit-learn pytorch torchvision gevent websocket-client websockets 
      or-tools beautifulsoup4
    ]);
    project-docs    = [ python39Packages.diagrams ]; 
    sys-libs        = [ openssl.dev zlib.dev file ];
    misc            = [ git-doc bashInteractive perl yasm ];
  };

  unstable-pkgs = with unstableChannel; { 
    persistence  = [ sqlite inotify-tools ]; 
  };

  # local-pkgs = with channel; {};

  native-build-inputs = (builtins.attrValues stable-pkgs) 
                     ++ (builtins.attrValues unstable-pkgs);
                   # ++ (builtins.attrValues local-pkgs);
in 
  shell-env {
    name = "development-environment"; 
    nativeBuildInputs = native-build-inputs;
    # shellHook = '' '';
  }
