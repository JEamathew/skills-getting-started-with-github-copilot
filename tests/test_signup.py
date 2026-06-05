"""Tests for the POST /activities/{activity_name}/signup endpoint using AAA pattern."""


def test_signup_success(client):
    """Test that a student can successfully sign up for an activity."""
    # Arrange
    email = "newstudent@mergington.edu"
    activity = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    data = response.json()
    
    # Assert
    assert response.status_code == 200
    assert "Signed up" in data["message"]
    assert email in data["message"]
    
    # Verify participant was added by fetching activities
    activities_response = client.get("/activities")
    assert email in activities_response.json()["Chess Club"]["participants"]


def test_signup_activity_not_found(client):
    """Test that signup returns 404 when activity does not exist."""
    # Arrange
    email = "student@mergington.edu"
    activity = "NonexistentActivity"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    data = response.json()
    
    # Assert
    assert response.status_code == 404
    assert "not found" in data["detail"].lower()


def test_signup_duplicate_email(client):
    """Test that signup returns 400 when email is already registered."""
    # Arrange
    email = "michael@mergington.edu"  # Already in Chess Club
    activity = "Chess Club"
    
    # Act
    response = client.post(
        f"/activities/{activity}/signup",
        params={"email": email}
    )
    data = response.json()
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in data["detail"].lower()


def test_signup_different_activity_after_first_signup(client):
    """Test that a student can sign up for a different activity after signing up for one."""
    # Arrange
    email = "newstudent@mergington.edu"
    first_activity = "Chess Club"
    second_activity = "Programming Class"
    
    # Act - Sign up for first activity
    response1 = client.post(
        f"/activities/{first_activity}/signup",
        params={"email": email}
    )
    
    # Act - Sign up for second activity
    response2 = client.post(
        f"/activities/{second_activity}/signup",
        params={"email": email}
    )
    
    # Assert both signups succeeded
    assert response1.status_code == 200
    assert response2.status_code == 200
    
    # Verify participant is in both activities
    activities_response = client.get("/activities")
    activities_data = activities_response.json()
    assert email in activities_data[first_activity]["participants"]
    assert email in activities_data[second_activity]["participants"]
