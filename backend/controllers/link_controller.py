from typing import List
from fastapi import HTTPException

from controllers.user_controller import UserController
from db.database_handler import DatabaseHandler
from exceptions.append_links_exception import AppendLinksException
from exceptions.update_user_data_exception import UpdateUserDataException
from models.link_model import LinkModel
from models.message_model import MessageModel


class LinkController:
    def __init__(
        self,
        database_controller: DatabaseHandler,
    ):
        self.__database_controller = database_controller
        self.__user_controller = UserController(database_controller)

    async def add_link(self, link: LinkModel, token: str) -> MessageModel:
        """Add a link to your account in another social network

        Args:
            link (LinkModel)
            token (str): access token

        Raises:
            HTTPException: If the link already exists or the link failed to add

        Returns:
            MessageModel
        """
        user = await self.__user_controller.get_user_by_token(token)
        result = list(filter(lambda item: link.url == item.url, user.links))
        if len(result) > 0:
            raise HTTPException(status_code=400, detail="Link already exists")

        try:
            await self.__database_controller.append_links_to_user(
                [link.dict()], user.key
            )
            return MessageModel(message="Link successfully added")
        except AppendLinksException as e:

            raise HTTPException(status_code=400, detail=f"{e}")

    async def remove_link(self, url_link: str, token: str) -> List[LinkModel]:
        """Delete a link to your account on another social network

        Args:
            url_link (str): 
            token (str): access token

        Raises:
            HTTPException: If the link is not found or the link failed to delete

        Returns:
            List[LinkModel]: Remaining links
        """        
        user = await self.__user_controller.get_user_by_token(token)
        result_find = list(filter(lambda item: url_link == item.url, user.links))
        if len(result_find) == 0:
            raise HTTPException(status_code=404, detail="Link not found")

        user.links.remove(result_find[0])
        try:
            await self.__database_controller.update_simple_data_to_user(
                {"links": (user.dict())["links"]}, user.key
            )
            return user.links
        except UpdateUserDataException as e:

            raise HTTPException(status_code=400, detail=f"{e}")
