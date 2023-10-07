from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_guilds_overview_response import MainGuildsOverviewResponse
from ...types import Response


def _get_kwargs(
    world: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/guilds/{world}".format(
            world=world,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainGuildsOverviewResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainGuildsOverviewResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainGuildsOverviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainGuildsOverviewResponse]:
    """List all guilds from a world

     Show all guilds on a certain world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainGuildsOverviewResponse]
    """

    kwargs = _get_kwargs(
        world=world,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainGuildsOverviewResponse]:
    """List all guilds from a world

     Show all guilds on a certain world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainGuildsOverviewResponse
    """

    return sync_detailed(
        world=world,
        client=client,
    ).parsed


async def asyncio_detailed(
    world: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainGuildsOverviewResponse]:
    """List all guilds from a world

     Show all guilds on a certain world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainGuildsOverviewResponse]
    """

    kwargs = _get_kwargs(
        world=world,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainGuildsOverviewResponse]:
    """List all guilds from a world

     Show all guilds on a certain world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainGuildsOverviewResponse
    """

    return (
        await asyncio_detailed(
            world=world,
            client=client,
        )
    ).parsed
