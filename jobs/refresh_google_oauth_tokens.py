from api_integrations import refresh_google_oauth_token
from data_access import (
    update_google_oauth_tokens_in_database,
    get_google_oauth_tokens,
)
from glue import (
    GoogleOAuthToken as GOAT_glue,
    GoogleScopeMap as GSM_glue,
    GoogleScope as GS_glue,
)


def refresh_google_oauth_tokens():
    old_oauth_tokens: list[tuple[GOAT_glue, int]] = get_google_oauth_tokens()
    new_oauth_tokens: list[tuple[GOAT_glue, int]] = list(
        map(
            lambda oauth_token: (
                refresh_google_oauth_token(oauth_token[0].refresh_token),
                oauth_token[1],
            ),
            old_oauth_tokens,
        )
    )
    update_google_oauth_tokens_in_database(new_oauth_tokens)
