from api_integrations import refresh_microsoft_oauth_token
from data_access import (
    update_microsoft_oauth_tokens_in_database,
    get_microsoft_oauth_tokens,
)
from glue import (
    MicrosoftOAuthToken as MOAT_glue,
    MicrosoftScopeMap as MSM_glue,
    MicrosoftScope as MS_glue,
)


def refresh_microsoft_oauth_tokens():
    old_oauth_tokens: list[tuple[MOAT_glue, int]] = get_microsoft_oauth_tokens()
    new_oauth_tokens: list[tuple[MOAT_glue, int]] = list(
        map(
            lambda oauth_token: (
                refresh_microsoft_oauth_token(
                    oauth_token[0].refresh_token, oauth_token[0].scopes
                ),
                oauth_token[1],
            ),
            old_oauth_tokens,
        )
    )
    update_microsoft_oauth_tokens_in_database(new_oauth_tokens)
