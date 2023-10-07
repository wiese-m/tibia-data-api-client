from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_v3_highscores_world_category_vocation_page_category import (
    GetV3HighscoresWorldCategoryVocationPageCategory,
)
from ...models.get_v3_highscores_world_category_vocation_page_vocation import (
    GetV3HighscoresWorldCategoryVocationPageVocation,
)
from ...models.main_highscores_response import MainHighscoresResponse
from ...types import Response


def _get_kwargs(
    world: str = "all",
    category: GetV3HighscoresWorldCategoryVocationPageCategory = GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE,
    vocation: GetV3HighscoresWorldCategoryVocationPageVocation = GetV3HighscoresWorldCategoryVocationPageVocation.ALL,
    page: int = 1,
) -> Dict[str, Any]:
    pass

    return {
        "method": "get",
        "url": "/v3/highscores/{world}/{category}/{vocation}/{page}".format(
            world=world,
            category=category,
            vocation=vocation,
            page=page,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[MainHighscoresResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MainHighscoresResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[MainHighscoresResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world: str = "all",
    category: GetV3HighscoresWorldCategoryVocationPageCategory = GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE,
    vocation: GetV3HighscoresWorldCategoryVocationPageVocation = GetV3HighscoresWorldCategoryVocationPageVocation.ALL,
    page: int = 1,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHighscoresResponse]:
    """Highscores of tibia

     Show all highscores of tibia

    Args:
        world (str):  Default: 'all'.
        category (GetV3HighscoresWorldCategoryVocationPageCategory):  Default:
            GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE.
        vocation (GetV3HighscoresWorldCategoryVocationPageVocation):  Default:
            GetV3HighscoresWorldCategoryVocationPageVocation.ALL.
        page (int):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHighscoresResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        category=category,
        vocation=vocation,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world: str = "all",
    category: GetV3HighscoresWorldCategoryVocationPageCategory = GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE,
    vocation: GetV3HighscoresWorldCategoryVocationPageVocation = GetV3HighscoresWorldCategoryVocationPageVocation.ALL,
    page: int = 1,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHighscoresResponse]:
    """Highscores of tibia

     Show all highscores of tibia

    Args:
        world (str):  Default: 'all'.
        category (GetV3HighscoresWorldCategoryVocationPageCategory):  Default:
            GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE.
        vocation (GetV3HighscoresWorldCategoryVocationPageVocation):  Default:
            GetV3HighscoresWorldCategoryVocationPageVocation.ALL.
        page (int):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHighscoresResponse
    """

    return sync_detailed(
        world=world,
        category=category,
        vocation=vocation,
        page=page,
        client=client,
    ).parsed


async def asyncio_detailed(
    world: str = "all",
    category: GetV3HighscoresWorldCategoryVocationPageCategory = GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE,
    vocation: GetV3HighscoresWorldCategoryVocationPageVocation = GetV3HighscoresWorldCategoryVocationPageVocation.ALL,
    page: int = 1,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MainHighscoresResponse]:
    """Highscores of tibia

     Show all highscores of tibia

    Args:
        world (str):  Default: 'all'.
        category (GetV3HighscoresWorldCategoryVocationPageCategory):  Default:
            GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE.
        vocation (GetV3HighscoresWorldCategoryVocationPageVocation):  Default:
            GetV3HighscoresWorldCategoryVocationPageVocation.ALL.
        page (int):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MainHighscoresResponse]
    """

    kwargs = _get_kwargs(
        world=world,
        category=category,
        vocation=vocation,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world: str = "all",
    category: GetV3HighscoresWorldCategoryVocationPageCategory = GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE,
    vocation: GetV3HighscoresWorldCategoryVocationPageVocation = GetV3HighscoresWorldCategoryVocationPageVocation.ALL,
    page: int = 1,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MainHighscoresResponse]:
    """Highscores of tibia

     Show all highscores of tibia

    Args:
        world (str):  Default: 'all'.
        category (GetV3HighscoresWorldCategoryVocationPageCategory):  Default:
            GetV3HighscoresWorldCategoryVocationPageCategory.EXPERIENCE.
        vocation (GetV3HighscoresWorldCategoryVocationPageVocation):  Default:
            GetV3HighscoresWorldCategoryVocationPageVocation.ALL.
        page (int):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MainHighscoresResponse
    """

    return (
        await asyncio_detailed(
            world=world,
            category=category,
            vocation=vocation,
            page=page,
            client=client,
        )
    ).parsed
