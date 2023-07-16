class Vod:

    def __init__(self, dict_json) -> None: 
       
        for key, value in dict_json.items():                    # add all the dict keys as attributes for this object,  does not work well with IntelliSense  
            setattr(self, key, value)

        self._extract_id()

    def _extract_id(self):
        nums = [char for char in self.url if char.isdigit()]              
        self.id = ''.join(nums)

    def __str__(self):           # like overriding toString() in java
        return f'{self.user_name}: {self.title}, {self.url} recorded on {self.created_at}'





json = "{'id': '1872645409', 'stream_id': '40901295048', 'user_id': '22484632', 'user_login': 'forsen', 'user_name': 'forsen', 'title': 'Games and shit!', 'description': '', 'created_at': '2023-07-15T16:02:23Z', 'published_at': '2023-07-15T16:02:23Z', 'url': 'https://www.twitch.tv/videos/1872645409', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/7e89cf034a2e580ae273_forsen_40901295048_1689436938//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 1422, 'language': 'en', 'type': 'archive', 'duration': '6h6m6s', 'muted_segments': None}"
obj = Vod(eval(json))
print(obj)                        

