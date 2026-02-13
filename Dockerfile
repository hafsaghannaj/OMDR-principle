# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # TeX Live for TikZ
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-pictures \
    # Python
    python3.11 \
    python3-pip \
    python3.11-venv \
    # Conversion tools
    pdf2svg \
    poppler-utils \
    imagemagick \
    ghostscript \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Allow ImageMagick to read/write PDFs
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml

# Set up Python virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3.11 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies
COPY scripts/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Deterministic PDF timestamps (avoids non-reproducible metadata)
ENV SOURCE_DATE_EPOCH=0

# Set working directory
WORKDIR /workspace

# Copy repository contents
COPY . .

# Default command: generate all figures
CMD ["bash", "scripts/generate_all.sh"]
