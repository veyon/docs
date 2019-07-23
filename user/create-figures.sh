#!/bin/sh

export VEYON_MASTER_CREATE_DOC_FIGURES=1
export QT_FONT_DPI=96

for i in en $(find ../locale/ -mindepth 1 -maxdepth 1 -type d -printf "%f\n") ; do
	export LANG=$i.UTF-8
	export LANGUAGE=$i
	mkdir -p images/$i
	cd images/$i
	veyon-master
	optipng -o9 Feature*png &
	optipng -o9 *Menu.png &
	optipng -o9 *Panel.png &
	optipng -o9 *Dialog*.png &
	optipng -o9 *Window.png &
	wait
	cd ../..
done

