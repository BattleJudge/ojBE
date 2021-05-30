from rest_framework.pagination import PageNumberPagination


class BattleRecordPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    page_query_param = 'page'


class RankPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    page_query_param = 'page'


class BattleSubmissionRecordPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
    page_query_param = 'page'