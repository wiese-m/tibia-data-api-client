from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_house_response import MainHouseResponse
from ...types import Response


def _get_kwargs(
    world: str,
    house_id: int,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/house/{world}/{house_id}".format(
            world=world,
            house_id=house_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainHouseResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainHouseResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainHouseResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world: str,
    house_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHouseResponse]:
    """House view

     Show all information about one house

    Args:
        world (str):
        house_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHouseResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        house_id=house_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world: str,
    house_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHouseResponse]:
    """House view

     Show all information about one house

    Args:
        world (str):
        house_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHouseResponse
    """

    return sync_detailed(
        world=world,
        house_id=house_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world: str,
    house_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHouseResponse]:
    """House view

     Show all information about one house

    Args:
        world (str):
        house_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHouseResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        house_id=house_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world: str,
    house_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHouseResponse]:
    """House view

     Show all information about one house

    Args:
        world (str):
        house_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHouseResponse
    """

    return (
        await asyncio_detailed(
            world=world,
            house_id=house_id,
            client=client,
        )
    ).parsed
