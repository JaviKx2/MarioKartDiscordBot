class SubmittedTime:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__id = kwargs.get('id')
        self.__time = kwargs.get('time')
        self.__approved = kwargs.get('approved')
        self.__pic_url = kwargs.get('pic_url')
        self.__ctgp_url = kwargs.get('ctgp_url')
        self.__timetrial_competition_id = kwargs.get('timetrial_competition_id')
