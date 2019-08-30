# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.chdfs.v20190718 import models


class ChdfsClient(AbstractClient):
    _apiVersion = '2019-07-18'
    _endpoint = 'chdfs.tencentcloudapi.com'


    def CreateAccessGroup(self, request):
        """创建权限组

        :param request: 调用CreateAccessGroup所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccessRules(self, request):
        """批量创建权限规则

        :param request: 调用CreateAccessRules所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFileSystem(self, request):
        """创建文件系统（异步创建）

        :param request: 调用CreateFileSystem所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileSystemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMountPoint(self, request):
        """创建挂载点

        :param request: 调用CreateMountPoint所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMountPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccessGroup(self, request):
        """删除权限组

        :param request: 调用DeleteAccessGroup所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccessRules(self, request):
        """批量删除权限规则

        :param request: 调用DeleteAccessRules所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFileSystem(self, request):
        """删除文件系统

        :param request: 调用DeleteFileSystem所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFileSystemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMountPoint(self, request):
        """删除挂载点

        :param request: 调用DeleteMountPoint所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessGroups(self, request):
        """查看权限组列表

        :param request: 调用DescribeAccessGroups所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccessRules(self, request):
        """查看权限规则列表

        :param request: 调用DescribeAccessRules所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileSystem(self, request):
        """查看文件系统详细信息

        :param request: 调用DescribeFileSystem所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileSystems(self, request):
        """查看文件系统列表

        :param request: 调用DescribeFileSystems所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMountPoint(self, request):
        """查看挂载点详细信息

        :param request: 调用DescribeMountPoint所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMountPoints(self, request):
        """查看挂载点列表

        :param request: 调用DescribeMountPoints所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessGroup(self, request):
        """修改权限组属性

        :param request: 调用ModifyAccessGroup所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccessRules(self, request):
        """批量修改权限规则属性

        :param request: 调用ModifyAccessRules所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFileSystem(self, request):
        """修改文件系统属性

        :param request: 调用ModifyFileSystem所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFileSystemResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMountPoint(self, request):
        """修改挂载点属性

        :param request: 调用ModifyMountPoint所需参数的结构体。
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMountPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)