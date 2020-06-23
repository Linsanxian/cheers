import {httpGet} from "./http";
import {httpPost} from "./http";

export const GetVersionList = (params = {}) => httpGet({ url: 'api/versions', params })


