from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_creature_response import MainCreatureResponse
from ...types import Response


def _get_kwargs(
    race: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/creature/{race}".format(
            race=race,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainCreatureResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainCreatureResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainCreatureResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    race: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainCreatureResponse]:
    """Show one creature

     Show all information about one creature

    Args:
        race (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainCreatureResponse]
    """

    kwargs = _get_kwargs(
        race=race,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    race: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainCreatureResponse]:
    """Show one creature

     Show all information about one creature

    Args:
        race (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainCreatureResponse
    """

    return sync_detailed(
        race=race,
        client=client,
    ).parsed


async def asyncio_detailed(
    race: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainCreatureResponse]:
    """Show one creature

     Show all information about one creature

    Args:
        race (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainCreatureResponse]
    """

    kwargs = _get_kwargs(
        race=race,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    race: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainCreatureResponse]:
    """Show one creature

     Show all information about one creature

    Args:
        race (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainCreatureResponse
    """

    return (
        await asyncio_detailed(
            race=race,
            client=client,
        )
    ).parsed
