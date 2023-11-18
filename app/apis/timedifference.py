from datetime import date, datetime

from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas import timedifference

router = APIRouter()


@router.get("/")
def get_time_difference(
    req: timedifference.GetTimeDifferenceRequest = Depends(),
) -> timedifference.GetTimeDifferenceResponse:
    # datetime.timeオブジェクトでは日付の差分が計算できないのでdatetime.datetimeを使用する
    now_date = date.today()
    date_value = [now_date.year, now_date.month, now_date.day]

    start_datetime = datetime(
        *date_value,
        hour=int(req.start_hour.value),
        minute=int(req.start_minute.value),
    )
    end_datetime = datetime(
        *date_value,
        hour=int(req.end_hour.value),
        minute=int(req.end_minute.value),
    )

    if end_datetime < start_datetime:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[
                {
                    "loc": ["start_hour, start_minute, end_hour or end_minute"],
                    "msg": "Please confirm your entry.",
                    "type": "value_error",
                }
            ],
        )

    timedelta_value = end_datetime - start_datetime

    return {"over_time": f"{timedelta_value.seconds / 3600}h"}
