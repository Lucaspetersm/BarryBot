from platform import system

VER = "3.0dev2"

USER_AGENT = (
  system().lower() +
  ":pw.yalnix.barry:" +
  VER +
  " by /u/Yalnix"
)

EVENTS = (
    "on_ready",
    "on_resumed",
    "on_error",
    "on_message",
    "on_socket_raw_receive",
    "on_socket_raw_send",
    "on_message_delete",
    "on_message_edit",
    "on_reaction_add",
    "on_reaction_remove",
    "on_reaction_clear",
    "on_channel_delete",
    "on_channel_create",
    "on_channel_update",
    "on_member_join",
    "on_member_remove",
    "on_member_update",
    "on_server_join",
    "on_server_remove",
    "on_server_update",
    "on_server_role_create",
    "on_server_role_delete",
    "on_server_role_update",
    "on_server_emojis_update",
    "on_server_available",
    "on_server_unavailable",
    "on_voice_state_update",
    "on_member_ban",
    "on_member_unban",
    "on_typing",
    "on_group_join",
    "on_group_remove"
)
