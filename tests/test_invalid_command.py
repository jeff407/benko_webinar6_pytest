def test_wrong_command(device):
    r = device.command("WRONG_COMMAND")
    assert r["status"] == "ERROR"
    assert r["code"] == "UNKNOWN_COMMAND"
