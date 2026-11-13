# container-supply-chain

A small, working example of **software supply-chain security** for a container image, built with GitHub Actions.

On every push to `main` the pipeline:

1. **Builds** a Docker image and pushes it to GitHub Container Registry (`ghcr.io`).
2. **Generates an SBOM** (Software Bill of Materials) in SPDX format with Syft.
3. **Scans** the image for critical and high vulnerabilities with Trivy.
4. **Signs** the image with Sigstore **cosign**, keyless (GitHub's OIDC identity, no long-lived keys).
5. **Attaches the SBOM** to the image as a signed attestation.
6. **Verifies** the signature and the attestation, pinned to this repository's workflow identity.

## Verify it yourself

```bash
IMAGE=ghcr.io/farkhanda-sadaf/container-supply-chain@<digest>
cosign verify "$IMAGE" \
  --certificate-identity https://github.com/farkhanda-sadaf/container-supply-chain/.github/workflows/supply-chain.yml@refs/heads/main \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com
```

The SBOM is also uploaded as a workflow artifact on each run.

## Files

| File | Purpose |
|---|---|
| `app.py` | Tiny Python health-check service (`/health`) |
| `Dockerfile` | Slim Python image, runs as a non-root user |
| `.github/workflows/supply-chain.yml` | Build → SBOM → scan → sign → attest → verify |
