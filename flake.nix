
{
  description = "rowanch site";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
      {
        devShells.${system}.default =  pkgs.mkShell 
        {
          venvDir = "./.venv";
          packages = [
            pkgs.python311
            pkgs.python311Packages.pip
            pkgs.python311Packages.venvShellHook
            pkgs.python311Packages.pillow
            pkgs.python311Packages.markdown
            pkgs.python311Packages.pelican
            pkgs.nodePackages_latest.tailwindcss

            pkgs.pyright
          ];
          postVenvCreation = ''
            unset SOURCE_DATE_EPOCH
          '';
        };
      };
}
