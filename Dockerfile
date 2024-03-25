FROM debian:bookworm-slim
MAINTAINER Tobias Junghans <tobydox@veyon.io>

RUN \
	apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
		make python3-sphinx sphinx-intl python3-sphinx-rtd-theme \
		fonts-linuxlibertine \
		gettext \
		latexmk \
		texlive-xetex \
		texlive-latex-recommended \
		texlive-fonts-recommended \
		texlive-fonts-extra \
		texlive-latex-extra \
		texlive-lang-cyrillic \
		texlive-lang-european \
		texlive-lang-french \
		texlive-lang-german \
		texlive-lang-italian \
		texlive-lang-spanish \
		xindy \
		&& \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/*

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8
