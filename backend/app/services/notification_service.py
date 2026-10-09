from typing import Optional

from sqlalchemy.orm import Session

from app.models.notification import Notification, NotificationType


def create_notification(
    db: Session,
    user_id: int,
    title: str,
    message: str,
    type: NotificationType = NotificationType.SYSTEM,
    commit: bool = True,
) -> Notification:
    """Create and persist a notification for a user."""
    notification = Notification(
        user_id=user_id,
        title=title,
        message=message,
        type=type,
    )
    db.add(notification)
    if commit:
        db.commit()
        db.refresh(notification)
    return notification


def create_booking_confirmation(
    db: Session,
    user_id: int,
    event_title: str,
    quantity: int,
    total_price: float,
    booking_id: int,
) -> Notification:
    return create_notification(
        db=db,
        user_id=user_id,
        title="Booking Confirmed",
        message=(
            f"Your booking #{booking_id} for '{event_title}' "
            f"({quantity} ticket(s), ${total_price:.2f}) is confirmed. "
            "Your QR tickets are ready."
        ),
        type=NotificationType.BOOKING,
        commit=False,
    )


def create_event_reminder(
    db: Session, user_id: int, event_title: str, event_date: Optional[str] = None
) -> Notification:
    when = f" on {event_date}" if event_date else ""
    return create_notification(
        db=db,
        user_id=user_id,
        title="Event Reminder",
        message=f"Don't forget: '{event_title}' is coming up{when}.",
        type=NotificationType.EVENT,
        commit=False,
    )
