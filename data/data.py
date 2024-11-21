class Basic:
    host = 'http://note-api.wps.cn'
    userid1 = 380493413
    sid1 = 'V02SLhq3OBmoksCi_G89b13NGYSK8bo00a6f3d6f0016adde65'
    userid2 = 380493419
    sid2 = 'V02SLhq3OBmoksCi_G89b13NGYSK8bo00a6f3d6f0016adde6p'


class Url:
    host = 'http://note-api.wps.cn'
    url_delete_note = host + '/v3/notesvr/delete'
    url_note_info = host + '/v3/notesvr/set/noteinfo'
    url_note_body = host + '/v3/notesvr/get/notebody'
    url_update_note_content = host + '/v3/notesvr/set/notecontent'
    url_remind = host + '/v3/notesvr/web/getnotes/remind'
    url_create_group = host + '/v3/notesvr/set/notegroup'
    url_delete_group = host + '/notesvr/delete/notegroup'
    url_get_groups = host + '/v3/notesvr/get/notegroup'
    url_get_group_notes = host + '/v3/notesvr/web/getnotes/remind'
    url_clean_recyclebin = host + '/v3/notesvr/cleanrecyclebin'

