from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.main_news_list_response import MainNewsListResponse
from ...types import Response


def _get_kwargs(
    days: int = 90,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/news/archive/{days}".format(
            days=days,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainNewsListResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainNewsListResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainNewsListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    days: int = 90,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainNewsListResponse]:
    """Show news archive (with days filter)

     Show news archive with a filtering option on days

    Args:
        days (int):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainNewsListResponse]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    days: int = 90,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainNewsListResponse]:
    """Show news archive (with days filter)

     Show news archive with a filtering option on days

    Args:
        days (int):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainNewsListResponse
    """

    return sync_detailed(
        days=days,
        client=client,
    ).parsed


async def asyncio_detailed(
    days: int = 90,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainNewsListResponse]:
    """Show news archive (with days filter)

     Show news archive with a filtering option on days

    Args:
        days (int):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainNewsListResponse]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    days: int = 90,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainNewsListResponse]:
    """Show news archive (with days filter)

     Show news archive with a filtering option on days

    Args:
        days (int):  Default: 90.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainNewsListResponse
    """

    return (
        await asyncio_detailed(
            days=days,
            client=client,
        )
    ).parsed
