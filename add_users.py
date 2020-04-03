# -*- coding: utf-8 -*-
# @createTime    : 2020/4/2 16:00
# @author  : Huanglg
# @fileName: add_users.py
# @email: luguang.huang@mabotech.com
import gitlab
import constants


def add_user(user_info):
    """

    :param user_info: {'email':email, 'username':username, 'name':name, 'password':password}
    :return:
    """
    gl = gitlab.Gitlab(url=constants.HOSTS,
                       private_token=constants.ACCESS_TOKEN,
                       api_version=constants.API_VERSION
                       )
    try:
        return gl.users.create(user_info)
    except Exception as e:
        print(e)
        raise


if __name__ == '__main__':

    user_info = {
        'email': 'abc@abc.com',
        'username': 'abc',
        'name': 'abc',
        'password': 'abc123456',
        'skip_confirmation': True
    }
    res = add_user(user_info)

