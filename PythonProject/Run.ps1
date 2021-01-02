REM Locally test mapper and reducers


type appleStock.txt | mapperAVG.py
type appleStock.txt | mapperAVG.py > mapper_output.txt

type appleStock.txt | mapperAVG.py | sort | reducerAVG.py
type appleStock.txt | mapperAVG.py | sort | reducerAVG.py > AppleAvg_ReducerOutput.txt

type appleStock.txt | mapperTvol.py
type appleStock.txt | mapperTvol.py > mapper_output.txt

type appleStock.txt | mapperTvol.py | sort | reducerTvol.py
type appleStock.txt | mapperTvol.py | sort | reducerTvol.py > AppleTotalVolume_ReducerOutput.txt

type ibmStock.txt | mapperAVG.py
type ibmStock.txt | mapperAVG.py > mapper_output.txt

type ibmStock.txt | mapperAVG.py | sort | reducerAVG.py
type ibmStock.txt | mapperAVG.py | sort | reducerAVG.py > IbmAvg_ReducerOutput.txt

type ibmStock.txt | mapperTvol.py
type ibmStock.txt | mapperTvol.py > mapper_output.txt

type ibmStock.txt | mapperTvol.py | sort | reducerTvol.py
type ibmStock.txt | mapperTvol.py | sort | reducerTvol.py > IbmTotalVolume_ReducerOutput.txt

type intelStock.txt | mapperAVG.py
type intelStock.txt | mapperAVG.py > mapper_output.txt

type intelStock.txt | mapperAVG.py | sort | reducerAVG.py
type intelStock.txt | mapperAVG.py | sort | reducerAVG.py > IntelAvg_ReducerOutput.txt

type intelStock.txt | mapperTvol.py
type intelStock.txt | mapperTvol.py > mapper_output.txt

type intelStock.txt | mapperTvol.py | sort | reducerTvol.py
type intelStock.txt | mapperTvol.py | sort | reducerTvol.py > IntelTotalVolume_ReducerOutput.txt

type microsoftStock.txt | mapperAVG.py
type microsoftStock.txt | mapperAVG.py > mapper_output.txt

type microsoftStock.txt | mapperAVG.py | sort | reducerAVG.py
type microsoftStock.txt | mapperAVG.py | sort | reducerAVG.py > MicrosoftAvg_ReducerOutput.txt

type microsoftStock.txt | mapperTvol.py
type microsoftStock.txt | mapperTvol.py > mapper_output.txt

type microsoftStock.txt | mapperTvol.py | sort | reducerTvol.py
type microsoftStock.txt | mapperTvol.py | sort | reducerTvol.py > MicrosoftTotalVolume_ReducerOutput.txt
