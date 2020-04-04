with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "trezor-firmware-hardware-tests";
  buildInputs = [ uhubctl ffmpeg pipenv ];
  NIX_ENFORCE_PURITY = 0;
}
