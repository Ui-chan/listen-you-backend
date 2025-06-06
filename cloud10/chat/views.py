from rest_framework.views import APIView
from rest_framework.response import Response
import uuid
from datetime import datetime

class RandomHashView(APIView):
    def get(self, request):
        """c_로 시작하는 랜덤 해시값 생성"""
        current_time = datetime.now()
        # 현재 시간을 마이크로초까지 포함한 타임스탬프로 변환
        timestamp = int(current_time.timestamp() * 100000)  # 마이크로초 단위로 변환

        # 타임스탬프를 16진수로 변환하고 8자리만 사용
        time_hash = hex(timestamp)[2:10]
        
        random_hash = f"c_{time_hash}"
        
        return Response({
            'counsel_id': random_hash,
            'created_at': current_time.strftime('%Y-%m-%d %H:%M:%S')  # 초 단위까지만 표시
        })
