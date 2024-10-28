#!/usr/bin/env bash

# Takes a 1024x1024 png image and generates an .icns bundle with all the various icon sizes in it.
# Usage: mkicon.sh /path/to/image.png
# Output is saved next to the input file as .icns file

input=$1
filename=$(basename "${input}" .png)
iconset="$(dirname "${input}")/${filename}.iconset"
outfile="$(dirname "${iconset}")/${filename}.icns"

echo "Input file: ${input}"
echo "Filename: ${filename}"
echo "Iconset dir: ${iconset}"
echo "Output file: ${outfile}"

mkdir -p "${iconset}"

sips --resampleHeightWidth 16 16     "${input}" --out "${iconset}/icon_16x16.png"
sips --resampleHeightWidth 32 32     "${input}" --out "${iconset}/icon_16x16@2x.png"
sips --resampleHeightWidth 32 32     "${input}" --out "${iconset}/icon_32x32.png"
sips --resampleHeightWidth 64 64     "${input}" --out "${iconset}/icon_32x32@2x.png"
sips --resampleHeightWidth 128 128   "${input}" --out "${iconset}/icon_128x128.png"
sips --resampleHeightWidth 256 256   "${input}" --out "${iconset}/icon_128x128@2x.png"
sips --resampleHeightWidth 256 256   "${input}" --out "${iconset}/icon_256x256.png"
sips --resampleHeightWidth 512 512   "${input}" --out "${iconset}/icon_256x256@2x.png"
sips --resampleHeightWidth 512 512   "${input}" --out "${iconset}/icon_512x512.png"
cp "${input}" "${iconset}/icon_512x512@2x.png"

iconutil -c icns "${iconset}" --out "${outfile}"
rm -r "${iconset}"
