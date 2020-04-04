with import (fetchTarball {
  url = "https://github.com/nixos/nixpkgs-channels/archive/c4adeddb5f8e945517068968d06ea838b7c24bd3.tar.gz";
  sha256 = "1vpm73y7d0j2cviq0cgjwdj64h2v0c349capiyqf5f6071anx7d7";
}) { };

stdenv.mkDerivation rec {
  name = "trezor-firmware-hardware-tests";
  buildInputs = [ uhubctl ffmpeg pipenv ];
}
