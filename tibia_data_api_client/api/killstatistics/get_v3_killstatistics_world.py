from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_kill_statistics_response import MainKillStatisticsResponse
from ...types import Response


def _get_kwargs(
    world: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/killstatistics/{world}".format(
            world=world,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainKillStatisticsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainKillStatisticsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainKillStatisticsResponse]:
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
) -> Response[MainKillStatisticsResponse]:
    """The killstatistics

     Show all killstatistics filtered on world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainKillStatisticsResponse]
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
) -> Optional[MainKillStatisticsResponse]:
    """The killstatistics

     Show all killstatistics filtered on world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainKillStatisticsResponse
    """

    return sync_detailed(
        world=world,
        client=client,
    ).parsed


async def asyncio_detailed(
    world: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainKillStatisticsResponse]:
    """The killstatistics

     Show all killstatistics filtered on world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainKillStatisticsResponse]
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
) -> Optional[MainKillStatisticsResponse]:
    """The killstatistics

     Show all killstatistics filtered on world

    Args:
        world (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainKillStatisticsResponse
    """

    return (
        await asyncio_detailed(
            world=world,
            client=client,
        )
    ).parsed
