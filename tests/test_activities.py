"""Tests for the GET /activities endpoint using AAA pattern."""


def test_get_activities_success(client):
    """Test that GET /activities returns all activities successfully."""
    # Arrange
    expected_activities = {"Chess Club", "Programming Class"}
    
    # Act
    response = client.get("/activities")
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert set(data.keys()) == expected_activities
    assert "participants" in data["Chess Club"]
    assert "schedule" in data["Chess Club"]


def test_get_activities_structure(client):
    """Test that activity objects have the correct structure."""
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}
    
    # Act
    response = client.get("/activities")
    data = response.json()
    activity = data["Chess Club"]
    
    # Assert
    assert response.status_code == 200
    assert set(activity.keys()) == required_keys
    assert isinstance(activity["participants"], list)
    assert isinstance(activity["max_participants"], int)


def test_get_activities_contains_participants(client):
    """Test that activities include participant data."""
    # Arrange
    expected_participant = "michael@mergington.edu"
    
    # Act
    response = client.get("/activities")
    data = response.json()
    chess_club_participants = data["Chess Club"]["participants"]
    
    # Assert
    assert response.status_code == 200
    assert expected_participant in chess_club_participants
