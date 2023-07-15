from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from texting import putText


def set_volume(level): # 볼륨 조절 함수 
    devices = AudioUtilities.GetSpeakers() # 시스템의 오디오 장치 불러오기
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) 
    # 'IAudioEndpointVolume'인터페이스 활성화
    volume = cast(interface, POINTER(IAudioEndpointVolume)) # 포인터 지정
    volume.SetMasterVolumeLevel(level, None) # 볼륨 레벨 설정 (단위 dB)
