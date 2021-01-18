# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeedMessage(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def header(self) -> type___FeedHeader: ...

    @property
    def entity(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___FeedEntity]: ...

    def __init__(self,
        *,
        header : typing___Optional[type___FeedHeader] = None,
        entity : typing___Optional[typing___Iterable[type___FeedEntity]] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"header",b"header"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"entity",b"entity",u"header",b"header"]) -> None: ...
type___FeedMessage = FeedMessage

class FeedHeader(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    IncrementalityValue = typing___NewType('IncrementalityValue', builtin___int)
    type___IncrementalityValue = IncrementalityValue
    Incrementality: _Incrementality
    class _Incrementality(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[FeedHeader.IncrementalityValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        FULL_DATASET = typing___cast(FeedHeader.IncrementalityValue, 0)
        DIFFERENTIAL = typing___cast(FeedHeader.IncrementalityValue, 1)
    FULL_DATASET = typing___cast(FeedHeader.IncrementalityValue, 0)
    DIFFERENTIAL = typing___cast(FeedHeader.IncrementalityValue, 1)
    type___Incrementality = Incrementality

    gtfs_realtime_version: typing___Text = ...
    incrementality: type___FeedHeader.IncrementalityValue = ...
    timestamp: builtin___int = ...

    def __init__(self,
        *,
        gtfs_realtime_version : typing___Optional[typing___Text] = None,
        incrementality : typing___Optional[type___FeedHeader.IncrementalityValue] = None,
        timestamp : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"gtfs_realtime_version",b"gtfs_realtime_version",u"incrementality",b"incrementality",u"timestamp",b"timestamp"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"gtfs_realtime_version",b"gtfs_realtime_version",u"incrementality",b"incrementality",u"timestamp",b"timestamp"]) -> None: ...
type___FeedHeader = FeedHeader

class FeedEntity(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    is_deleted: builtin___bool = ...

    @property
    def trip_update(self) -> type___TripUpdate: ...

    @property
    def vehicle(self) -> type___VehiclePosition: ...

    @property
    def alert(self) -> type___Alert: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        is_deleted : typing___Optional[builtin___bool] = None,
        trip_update : typing___Optional[type___TripUpdate] = None,
        vehicle : typing___Optional[type___VehiclePosition] = None,
        alert : typing___Optional[type___Alert] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"alert",b"alert",u"id",b"id",u"is_deleted",b"is_deleted",u"trip_update",b"trip_update",u"vehicle",b"vehicle"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"alert",b"alert",u"id",b"id",u"is_deleted",b"is_deleted",u"trip_update",b"trip_update",u"vehicle",b"vehicle"]) -> None: ...
type___FeedEntity = FeedEntity

class TripUpdate(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class StopTimeEvent(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        delay: builtin___int = ...
        time: builtin___int = ...
        uncertainty: builtin___int = ...

        def __init__(self,
            *,
            delay : typing___Optional[builtin___int] = None,
            time : typing___Optional[builtin___int] = None,
            uncertainty : typing___Optional[builtin___int] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"delay",b"delay",u"time",b"time",u"uncertainty",b"uncertainty"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"delay",b"delay",u"time",b"time",u"uncertainty",b"uncertainty"]) -> None: ...
    type___StopTimeEvent = StopTimeEvent

    class StopTimeUpdate(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        ScheduleRelationshipValue = typing___NewType('ScheduleRelationshipValue', builtin___int)
        type___ScheduleRelationshipValue = ScheduleRelationshipValue
        ScheduleRelationship: _ScheduleRelationship
        class _ScheduleRelationship(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TripUpdate.StopTimeUpdate.ScheduleRelationshipValue]):
            DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
            SCHEDULED = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 0)
            SKIPPED = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 1)
            NO_DATA = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 2)
        SCHEDULED = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 0)
        SKIPPED = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 1)
        NO_DATA = typing___cast(TripUpdate.StopTimeUpdate.ScheduleRelationshipValue, 2)
        type___ScheduleRelationship = ScheduleRelationship

        stop_sequence: builtin___int = ...
        stop_id: typing___Text = ...
        schedule_relationship: type___TripUpdate.StopTimeUpdate.ScheduleRelationshipValue = ...

        @property
        def arrival(self) -> type___TripUpdate.StopTimeEvent: ...

        @property
        def departure(self) -> type___TripUpdate.StopTimeEvent: ...

        def __init__(self,
            *,
            stop_sequence : typing___Optional[builtin___int] = None,
            stop_id : typing___Optional[typing___Text] = None,
            arrival : typing___Optional[type___TripUpdate.StopTimeEvent] = None,
            departure : typing___Optional[type___TripUpdate.StopTimeEvent] = None,
            schedule_relationship : typing___Optional[type___TripUpdate.StopTimeUpdate.ScheduleRelationshipValue] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"arrival",b"arrival",u"departure",b"departure",u"schedule_relationship",b"schedule_relationship",u"stop_id",b"stop_id",u"stop_sequence",b"stop_sequence"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"arrival",b"arrival",u"departure",b"departure",u"schedule_relationship",b"schedule_relationship",u"stop_id",b"stop_id",u"stop_sequence",b"stop_sequence"]) -> None: ...
    type___StopTimeUpdate = StopTimeUpdate

    timestamp: builtin___int = ...
    delay: builtin___int = ...

    @property
    def trip(self) -> type___TripDescriptor: ...

    @property
    def vehicle(self) -> type___VehicleDescriptor: ...

    @property
    def stop_time_update(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TripUpdate.StopTimeUpdate]: ...

    def __init__(self,
        *,
        trip : typing___Optional[type___TripDescriptor] = None,
        vehicle : typing___Optional[type___VehicleDescriptor] = None,
        stop_time_update : typing___Optional[typing___Iterable[type___TripUpdate.StopTimeUpdate]] = None,
        timestamp : typing___Optional[builtin___int] = None,
        delay : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"delay",b"delay",u"timestamp",b"timestamp",u"trip",b"trip",u"vehicle",b"vehicle"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"delay",b"delay",u"stop_time_update",b"stop_time_update",u"timestamp",b"timestamp",u"trip",b"trip",u"vehicle",b"vehicle"]) -> None: ...
type___TripUpdate = TripUpdate

class VehiclePosition(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    VehicleStopStatusValue = typing___NewType('VehicleStopStatusValue', builtin___int)
    type___VehicleStopStatusValue = VehicleStopStatusValue
    VehicleStopStatus: _VehicleStopStatus
    class _VehicleStopStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[VehiclePosition.VehicleStopStatusValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        INCOMING_AT = typing___cast(VehiclePosition.VehicleStopStatusValue, 0)
        STOPPED_AT = typing___cast(VehiclePosition.VehicleStopStatusValue, 1)
        IN_TRANSIT_TO = typing___cast(VehiclePosition.VehicleStopStatusValue, 2)
    INCOMING_AT = typing___cast(VehiclePosition.VehicleStopStatusValue, 0)
    STOPPED_AT = typing___cast(VehiclePosition.VehicleStopStatusValue, 1)
    IN_TRANSIT_TO = typing___cast(VehiclePosition.VehicleStopStatusValue, 2)
    type___VehicleStopStatus = VehicleStopStatus

    CongestionLevelValue = typing___NewType('CongestionLevelValue', builtin___int)
    type___CongestionLevelValue = CongestionLevelValue
    CongestionLevel: _CongestionLevel
    class _CongestionLevel(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[VehiclePosition.CongestionLevelValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN_CONGESTION_LEVEL = typing___cast(VehiclePosition.CongestionLevelValue, 0)
        RUNNING_SMOOTHLY = typing___cast(VehiclePosition.CongestionLevelValue, 1)
        STOP_AND_GO = typing___cast(VehiclePosition.CongestionLevelValue, 2)
        CONGESTION = typing___cast(VehiclePosition.CongestionLevelValue, 3)
        SEVERE_CONGESTION = typing___cast(VehiclePosition.CongestionLevelValue, 4)
    UNKNOWN_CONGESTION_LEVEL = typing___cast(VehiclePosition.CongestionLevelValue, 0)
    RUNNING_SMOOTHLY = typing___cast(VehiclePosition.CongestionLevelValue, 1)
    STOP_AND_GO = typing___cast(VehiclePosition.CongestionLevelValue, 2)
    CONGESTION = typing___cast(VehiclePosition.CongestionLevelValue, 3)
    SEVERE_CONGESTION = typing___cast(VehiclePosition.CongestionLevelValue, 4)
    type___CongestionLevel = CongestionLevel

    OccupancyStatusValue = typing___NewType('OccupancyStatusValue', builtin___int)
    type___OccupancyStatusValue = OccupancyStatusValue
    OccupancyStatus: _OccupancyStatus
    class _OccupancyStatus(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[VehiclePosition.OccupancyStatusValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        EMPTY = typing___cast(VehiclePosition.OccupancyStatusValue, 0)
        MANY_SEATS_AVAILABLE = typing___cast(VehiclePosition.OccupancyStatusValue, 1)
        FEW_SEATS_AVAILABLE = typing___cast(VehiclePosition.OccupancyStatusValue, 2)
        STANDING_ROOM_ONLY = typing___cast(VehiclePosition.OccupancyStatusValue, 3)
        CRUSHED_STANDING_ROOM_ONLY = typing___cast(VehiclePosition.OccupancyStatusValue, 4)
        FULL = typing___cast(VehiclePosition.OccupancyStatusValue, 5)
        NOT_ACCEPTING_PASSENGERS = typing___cast(VehiclePosition.OccupancyStatusValue, 6)
    EMPTY = typing___cast(VehiclePosition.OccupancyStatusValue, 0)
    MANY_SEATS_AVAILABLE = typing___cast(VehiclePosition.OccupancyStatusValue, 1)
    FEW_SEATS_AVAILABLE = typing___cast(VehiclePosition.OccupancyStatusValue, 2)
    STANDING_ROOM_ONLY = typing___cast(VehiclePosition.OccupancyStatusValue, 3)
    CRUSHED_STANDING_ROOM_ONLY = typing___cast(VehiclePosition.OccupancyStatusValue, 4)
    FULL = typing___cast(VehiclePosition.OccupancyStatusValue, 5)
    NOT_ACCEPTING_PASSENGERS = typing___cast(VehiclePosition.OccupancyStatusValue, 6)
    type___OccupancyStatus = OccupancyStatus

    current_stop_sequence: builtin___int = ...
    stop_id: typing___Text = ...
    current_status: type___VehiclePosition.VehicleStopStatusValue = ...
    timestamp: builtin___int = ...
    congestion_level: type___VehiclePosition.CongestionLevelValue = ...
    occupancy_status: type___VehiclePosition.OccupancyStatusValue = ...

    @property
    def trip(self) -> type___TripDescriptor: ...

    @property
    def vehicle(self) -> type___VehicleDescriptor: ...

    @property
    def position(self) -> type___Position: ...

    def __init__(self,
        *,
        trip : typing___Optional[type___TripDescriptor] = None,
        vehicle : typing___Optional[type___VehicleDescriptor] = None,
        position : typing___Optional[type___Position] = None,
        current_stop_sequence : typing___Optional[builtin___int] = None,
        stop_id : typing___Optional[typing___Text] = None,
        current_status : typing___Optional[type___VehiclePosition.VehicleStopStatusValue] = None,
        timestamp : typing___Optional[builtin___int] = None,
        congestion_level : typing___Optional[type___VehiclePosition.CongestionLevelValue] = None,
        occupancy_status : typing___Optional[type___VehiclePosition.OccupancyStatusValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"congestion_level",b"congestion_level",u"current_status",b"current_status",u"current_stop_sequence",b"current_stop_sequence",u"occupancy_status",b"occupancy_status",u"position",b"position",u"stop_id",b"stop_id",u"timestamp",b"timestamp",u"trip",b"trip",u"vehicle",b"vehicle"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"congestion_level",b"congestion_level",u"current_status",b"current_status",u"current_stop_sequence",b"current_stop_sequence",u"occupancy_status",b"occupancy_status",u"position",b"position",u"stop_id",b"stop_id",u"timestamp",b"timestamp",u"trip",b"trip",u"vehicle",b"vehicle"]) -> None: ...
type___VehiclePosition = VehiclePosition

class Alert(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CauseValue = typing___NewType('CauseValue', builtin___int)
    type___CauseValue = CauseValue
    Cause: _Cause
    class _Cause(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[Alert.CauseValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNKNOWN_CAUSE = typing___cast(Alert.CauseValue, 1)
        OTHER_CAUSE = typing___cast(Alert.CauseValue, 2)
        TECHNICAL_PROBLEM = typing___cast(Alert.CauseValue, 3)
        STRIKE = typing___cast(Alert.CauseValue, 4)
        DEMONSTRATION = typing___cast(Alert.CauseValue, 5)
        ACCIDENT = typing___cast(Alert.CauseValue, 6)
        HOLIDAY = typing___cast(Alert.CauseValue, 7)
        WEATHER = typing___cast(Alert.CauseValue, 8)
        MAINTENANCE = typing___cast(Alert.CauseValue, 9)
        CONSTRUCTION = typing___cast(Alert.CauseValue, 10)
        POLICE_ACTIVITY = typing___cast(Alert.CauseValue, 11)
        MEDICAL_EMERGENCY = typing___cast(Alert.CauseValue, 12)
    UNKNOWN_CAUSE = typing___cast(Alert.CauseValue, 1)
    OTHER_CAUSE = typing___cast(Alert.CauseValue, 2)
    TECHNICAL_PROBLEM = typing___cast(Alert.CauseValue, 3)
    STRIKE = typing___cast(Alert.CauseValue, 4)
    DEMONSTRATION = typing___cast(Alert.CauseValue, 5)
    ACCIDENT = typing___cast(Alert.CauseValue, 6)
    HOLIDAY = typing___cast(Alert.CauseValue, 7)
    WEATHER = typing___cast(Alert.CauseValue, 8)
    MAINTENANCE = typing___cast(Alert.CauseValue, 9)
    CONSTRUCTION = typing___cast(Alert.CauseValue, 10)
    POLICE_ACTIVITY = typing___cast(Alert.CauseValue, 11)
    MEDICAL_EMERGENCY = typing___cast(Alert.CauseValue, 12)
    type___Cause = Cause

    EffectValue = typing___NewType('EffectValue', builtin___int)
    type___EffectValue = EffectValue
    Effect: _Effect
    class _Effect(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[Alert.EffectValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        NO_SERVICE = typing___cast(Alert.EffectValue, 1)
        REDUCED_SERVICE = typing___cast(Alert.EffectValue, 2)
        SIGNIFICANT_DELAYS = typing___cast(Alert.EffectValue, 3)
        DETOUR = typing___cast(Alert.EffectValue, 4)
        ADDITIONAL_SERVICE = typing___cast(Alert.EffectValue, 5)
        MODIFIED_SERVICE = typing___cast(Alert.EffectValue, 6)
        OTHER_EFFECT = typing___cast(Alert.EffectValue, 7)
        UNKNOWN_EFFECT = typing___cast(Alert.EffectValue, 8)
        STOP_MOVED = typing___cast(Alert.EffectValue, 9)
    NO_SERVICE = typing___cast(Alert.EffectValue, 1)
    REDUCED_SERVICE = typing___cast(Alert.EffectValue, 2)
    SIGNIFICANT_DELAYS = typing___cast(Alert.EffectValue, 3)
    DETOUR = typing___cast(Alert.EffectValue, 4)
    ADDITIONAL_SERVICE = typing___cast(Alert.EffectValue, 5)
    MODIFIED_SERVICE = typing___cast(Alert.EffectValue, 6)
    OTHER_EFFECT = typing___cast(Alert.EffectValue, 7)
    UNKNOWN_EFFECT = typing___cast(Alert.EffectValue, 8)
    STOP_MOVED = typing___cast(Alert.EffectValue, 9)
    type___Effect = Effect

    cause: type___Alert.CauseValue = ...
    effect: type___Alert.EffectValue = ...

    @property
    def active_period(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TimeRange]: ...

    @property
    def informed_entity(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___EntitySelector]: ...

    @property
    def url(self) -> type___TranslatedString: ...

    @property
    def header_text(self) -> type___TranslatedString: ...

    @property
    def description_text(self) -> type___TranslatedString: ...

    def __init__(self,
        *,
        active_period : typing___Optional[typing___Iterable[type___TimeRange]] = None,
        informed_entity : typing___Optional[typing___Iterable[type___EntitySelector]] = None,
        cause : typing___Optional[type___Alert.CauseValue] = None,
        effect : typing___Optional[type___Alert.EffectValue] = None,
        url : typing___Optional[type___TranslatedString] = None,
        header_text : typing___Optional[type___TranslatedString] = None,
        description_text : typing___Optional[type___TranslatedString] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cause",b"cause",u"description_text",b"description_text",u"effect",b"effect",u"header_text",b"header_text",u"url",b"url"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"active_period",b"active_period",u"cause",b"cause",u"description_text",b"description_text",u"effect",b"effect",u"header_text",b"header_text",u"informed_entity",b"informed_entity",u"url",b"url"]) -> None: ...
type___Alert = Alert

class TimeRange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start: builtin___int = ...
    end: builtin___int = ...

    def __init__(self,
        *,
        start : typing___Optional[builtin___int] = None,
        end : typing___Optional[builtin___int] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"end",b"end",u"start",b"start"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"end",b"end",u"start",b"start"]) -> None: ...
type___TimeRange = TimeRange

class Position(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    latitude: builtin___float = ...
    longitude: builtin___float = ...
    bearing: builtin___float = ...
    odometer: builtin___float = ...
    speed: builtin___float = ...

    def __init__(self,
        *,
        latitude : typing___Optional[builtin___float] = None,
        longitude : typing___Optional[builtin___float] = None,
        bearing : typing___Optional[builtin___float] = None,
        odometer : typing___Optional[builtin___float] = None,
        speed : typing___Optional[builtin___float] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bearing",b"bearing",u"latitude",b"latitude",u"longitude",b"longitude",u"odometer",b"odometer",u"speed",b"speed"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bearing",b"bearing",u"latitude",b"latitude",u"longitude",b"longitude",u"odometer",b"odometer",u"speed",b"speed"]) -> None: ...
type___Position = Position

class TripDescriptor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ScheduleRelationshipValue = typing___NewType('ScheduleRelationshipValue', builtin___int)
    type___ScheduleRelationshipValue = ScheduleRelationshipValue
    ScheduleRelationship: _ScheduleRelationship
    class _ScheduleRelationship(google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[TripDescriptor.ScheduleRelationshipValue]):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        SCHEDULED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 0)
        ADDED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 1)
        UNSCHEDULED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 2)
        CANCELED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 3)
    SCHEDULED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 0)
    ADDED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 1)
    UNSCHEDULED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 2)
    CANCELED = typing___cast(TripDescriptor.ScheduleRelationshipValue, 3)
    type___ScheduleRelationship = ScheduleRelationship

    trip_id: typing___Text = ...
    route_id: typing___Text = ...
    direction_id: builtin___int = ...
    start_time: typing___Text = ...
    start_date: typing___Text = ...
    schedule_relationship: type___TripDescriptor.ScheduleRelationshipValue = ...

    def __init__(self,
        *,
        trip_id : typing___Optional[typing___Text] = None,
        route_id : typing___Optional[typing___Text] = None,
        direction_id : typing___Optional[builtin___int] = None,
        start_time : typing___Optional[typing___Text] = None,
        start_date : typing___Optional[typing___Text] = None,
        schedule_relationship : typing___Optional[type___TripDescriptor.ScheduleRelationshipValue] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"direction_id",b"direction_id",u"route_id",b"route_id",u"schedule_relationship",b"schedule_relationship",u"start_date",b"start_date",u"start_time",b"start_time",u"trip_id",b"trip_id"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"direction_id",b"direction_id",u"route_id",b"route_id",u"schedule_relationship",b"schedule_relationship",u"start_date",b"start_date",u"start_time",b"start_time",u"trip_id",b"trip_id"]) -> None: ...
type___TripDescriptor = TripDescriptor

class VehicleDescriptor(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    label: typing___Text = ...
    license_plate: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        label : typing___Optional[typing___Text] = None,
        license_plate : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"label",b"label",u"license_plate",b"license_plate"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"label",b"label",u"license_plate",b"license_plate"]) -> None: ...
type___VehicleDescriptor = VehicleDescriptor

class EntitySelector(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    agency_id: typing___Text = ...
    route_id: typing___Text = ...
    route_type: builtin___int = ...
    stop_id: typing___Text = ...

    @property
    def trip(self) -> type___TripDescriptor: ...

    def __init__(self,
        *,
        agency_id : typing___Optional[typing___Text] = None,
        route_id : typing___Optional[typing___Text] = None,
        route_type : typing___Optional[builtin___int] = None,
        trip : typing___Optional[type___TripDescriptor] = None,
        stop_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"agency_id",b"agency_id",u"route_id",b"route_id",u"route_type",b"route_type",u"stop_id",b"stop_id",u"trip",b"trip"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"agency_id",b"agency_id",u"route_id",b"route_id",u"route_type",b"route_type",u"stop_id",b"stop_id",u"trip",b"trip"]) -> None: ...
type___EntitySelector = EntitySelector

class TranslatedString(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Translation(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        text: typing___Text = ...
        language: typing___Text = ...

        def __init__(self,
            *,
            text : typing___Optional[typing___Text] = None,
            language : typing___Optional[typing___Text] = None,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"language",b"language",u"text",b"text"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"language",b"language",u"text",b"text"]) -> None: ...
    type___Translation = Translation


    @property
    def translation(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[type___TranslatedString.Translation]: ...

    def __init__(self,
        *,
        translation : typing___Optional[typing___Iterable[type___TranslatedString.Translation]] = None,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"translation",b"translation"]) -> None: ...
type___TranslatedString = TranslatedString
