from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_houses_overview_response import MainHousesOverviewResponse
from ...types import Response


def _get_kwargs(
    world: str,
    town: str,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/houses/{world}/{town}".format(
            world=world,
            town=town,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainHousesOverviewResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainHousesOverviewResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainHousesOverviewResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world: str,
    town: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHousesOverviewResponse]:
    """List of houses

     Show all houses filtered on world and town

    Args:
        world (str):
        town (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHousesOverviewResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        town=town,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world: str,
    town: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHousesOverviewResponse]:
    """List of houses

     Show all houses filtered on world and town

    Args:
        world (str):
        town (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHousesOverviewResponse
    """

    return sync_detailed(
        world=world,
        town=town,
        client=client,
    ).parsed


async def asyncio_detailed(
    world: str,
    town: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHousesOverviewResponse]:
    """List of houses

     Show all houses filtered on world and town

    Args:
        world (str):
        town (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHousesOverviewResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        town=town,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world: str,
    town: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHousesOverviewResponse]:
    """List of houses

     Show all houses filtered on world and town

    Args:
        world (str):
        town (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHousesOverviewResponse
    """

    return (
        await asyncio_detailed(
            world=world,
            town=town,
            client=client,
        )
    ).parsed
