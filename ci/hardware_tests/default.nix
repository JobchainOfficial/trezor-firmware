with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "trezor-firmware-hardware-tests";
  buildInputs = [ uhubctl ffmpeg pipenv ];
}
