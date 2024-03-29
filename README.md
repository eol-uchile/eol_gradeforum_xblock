# EOL Grade Forum XBlock

![https://github.com/eol-uchile/eol_gradeforum_xblock/actions](https://github.com/eol-uchile/eol_gradeforum_xblock/workflows/Python%20application/badge.svg)

This XBlock allow to grade the participation in the forum according to the student.

# Install

    docker-compose exec cms pip install -e /openedx/requirements/eol_gradeforum_xblock
    docker-compose exec lms pip install -e /openedx/requirements/eol_gradeforum_xblock

# Configuration

Edit *production.py* in *lms and cms settings* and set the limit_thread, this parameter configures the maximum number of publications that are obtained from a discussion.

    EOLGRADEFORUM_LIMIT_THREADS = 5000
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_WHITELIST = ['studio.domain.com']
    CORS_ALLOW_HEADERS = corsheaders_default_headers + (
        'use-jwt-cookie',
    )

## TESTS
**Prepare tests:**

    > cd .github/
    > docker-compose run --rm lms /openedx/requirements/eol_gradeforum_xblock/.github/test.sh
