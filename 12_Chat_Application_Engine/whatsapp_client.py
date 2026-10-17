import socket
import threading
import json
import sys
import time
import uuid

# =====================================================================
# 1. CORE WHATSAPP CLIENT INFRASTRUCTURE INTERFACE
# =====================================================================

class WhatsAppClient:
    def __init__(self, server_host: str = "127.0.0.1", server_port: int = 9999) -> None:
        """
        Initializes the client routing protocols and secure memory registers.
        """
        self.server_host = server_host
        self.server_port = server_port
        self.client_socket = None
        self.username = None
        self.is_connected = False
        
        # Inbound media call flags management configuration
        self.active_call_room = None
        self.in_active_call = False

    def initialize_session(self) -> None:
        """
        Establishes network handshake boundaries with the central WhatsAppHub server.
        """
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.server_host, self.server_port))
            
            print("\n====================================================")
            print("│            WELCOME TO ENTERPRISE WHATSAPP         │")
            print("====================================================")
            
            # Authentication Matrix Collection Node
            username_input = input("Enter Registered Username: ").strip().upper()
            password_input = input("Enter Secure Account Password Token: ").strip()

            auth_packet = json.dumps({
                "username": username_input,
                "token": password_input
            })
            
            # Pipes credential frame into the central core validation row layout
            self.client_socket.send(auth_packet.encode('utf-8'))
            
            # Evaluates system registration response metrics
            response = self.client_socket.recv(4096).decode('utf-8')
            response_data = json.loads(response)

            if response_data.get("status") == "SUCCESS":
                self.username = username_input
                self.is_connected = True
                print(f"\n[ACCESS GRANTED]: Welcome back, {self.username}! Connection locked.")
                
                # Spawns asynchronous non-blocking thread to ingest live streams concurrently
                threading.Thread(target=self.__inbound_packet_listener, daemon=True).start()
                
                # Routes the execution flow into the main interface row panel switcher
                self.launch_interface_loop()
            else:
                print(f"\n[ACCESS DENIED]: Authorization failed: {response_data.get('msg')}")
                self.client_socket.close()
                
        except Exception as e:
            print(f"\n[CRITICAL NETWORK ERROR]: Server unreachable or context dropped: {e}")

    def trigger_media_call_handshake(self, call_type: str = "VIDEO") -> None:
        """
        Generates structured peer token signaling to request audio/video conference sessions.
        """
        target_peer = input(f"Enter target user to {call_type} call: ").strip().upper()
        if not target_peer:
            return

        # Generates a completely unique corporate room allocation ID footprint token
        generated_room_id = str(uuid.uuid4())[:8]
        
        call_packet = json.dumps({
            "action": "INIT_CALL",
            "target": target_peer,
            "call_type": call_type,
            "room_id": generated_room_id
        })
        
        try:
            self.client_socket.send(call_packet.encode('utf-8'))
            print(f"\n[OUTBOUND CALL]: Dialing {target_peer} via {call_type} loop. Awaiting answer...")
            
            # Explicit override to mock runtime device loops inside console interfaces safely
            self.is_connected = False # Briefly pause interface loops during configuration
            self.__simulate_console_media_stream(generated_room_id, call_type, f"OUTBOUND TO {target_peer}")
            self.is_connected = True
        except Exception:
            print("[ERROR]: Signaling pipeline drop. Inbound target unreachable.")
    def __inbound_packet_listener(self) -> None:
        """
        Continuous asynchronous network listener thread parsing incoming traffic 
        from the Central Server without locking the user interface input fields.
        """
        while self.is_connected:
            try:
                raw_stream_data = self.client_socket.recv(4096).decode('utf-8')
                if not raw_stream_data:
                    print("\n[DISCONNECTED]: Connection closed down by Central Hub Server.")
                    self.is_connected = False
                    break

                packet = json.loads(raw_stream_data)
                action = packet.get("action", "")

                if action == "RECEIVE_PRIVATE":
                    # Prints single direct messaging vectors instantly onto the interface line rows
                    print(f"\n\r[{packet.get('timestamp')}] [DM] {packet.get('sender')}: {packet.get('msg')}")
                    print("\nChoice Option Selection Matrix Entry: ", end="", flush=True)

                elif action == "RECEIVE_GROUP":
                    # Prints group broadcast packets safely inside defined layout arrays
                    print(f"\n\r[{packet.get('timestamp')}] [GROUP: {packet.get('group')}] {packet.get('sender')}: {packet.get('msg')}")
                    print("\nChoice Option Selection Matrix Entry: ", end="", flush=True)

                elif action == "ALERT":
                    # Prints system driven administrative status flags directly
                    print(f"\n\r[SYSTEM ALERT]: {packet.get('msg')}")
                    print("\nChoice Option Selection Matrix Entry: ", end="", flush=True)

                elif action == "STATUS_LIST":
                    # Unpacks available active story matrices cached inside central networks
                    print("\n\n====================================================")
                    print("│          ACTIVE WHATSAPP STATUS STORIES VIEW     │")
                    print("====================================================")
                    story_map = packet.get("data", {})
                    if not story_map:
                        print("  No active text stories uploaded in the last 24 hours.")
                    for user, text in story_map.items():
                        print(f"  * {user:<15} : \"{text}\"")
                    print("====================================================")
                    print("\nChoice Option Selection Matrix Entry: ", end="", flush=True)

                elif action == "INBOUND_CALL":
                    # 👈 THE ULTIMATE REAL-TIME SIGNALING INTERCEPT GATEWAY
                    # As requested by user, this block instantly alerts target units about inbound calls
                    caller = packet.get("sender", "")
                    call_type = packet.get("call_type", "VIDEO")
                    room_id = packet.get("room_id", "")
                    
                    print(f"\n\n⚡" + "!" * 50)
                    print(f"! [INBOUND CALL ALERT]: {caller} IS DIALING YOU FOR A {call_type} CALL!")
                    print(f"! [ROOM REFERENCE   ]: {room_id}")
                    print("!" * 52)
                    
                    # Intercepting user prompt controls dynamically to ingest conference answer flag configurations
                    accept_flag = input(f"\nDo you want to accept this {call_type} call from {caller}? (Y/N): ").strip().upper()
                    
                    if accept_flag == "Y":
                        print(f"\n[CONNECTING]: Handshake bound. Booting {call_type} media peripheral buffers...")
                        self.__simulate_console_media_stream(room_id, call_type, f"INBOUND FROM {caller}")
                    else:
                        print("\n[CALL REJECTED]: Dropping signaling packets securely.")

            except Exception:
                print("\n[ALERT]: Inbound signaling listener pipeline context dropped.")
                self.is_connected = False
                break
    def launch_interface_loop(self) -> None:
        """
        Renders the corporate choice menu selector panel frames to route output requests sequentially.
        """
        while self.is_connected:
            try:
                print("\n====================================================")
                print(f"│       WHATSAPP INTERACTIVE DASHBOARD [{self.username}]       │")
                print("====================================================")
                print("  1. SEND PRIVATE DIRECT MESSAGE (DM)")
                print("  2. CREATE NEW WHATSAPP CHAT GROUP")
                print("  3. BROADCAST MESSAGE TO GROUP DOMAIN")
                print("  4. POST 24-HOUR ACTIVE STATUS STORY")
                print("  5. VIEW SYSTEM LIVE STATUS STORIES")
                print("  6. INITIATE SECURE AUDIO CALL")
                print("  7. INITIATE SECURE VIDEO CALL")
                print("  8. SHUT DOWN ACCOUNT SESSION (EXIT)")
                print("====================================================")
                
                choice = input("Choice Option Selection Matrix Entry: ").strip()

                if choice == "1":
                    self.__dispatch_private_message_packet()
                elif choice == "2":
                    self.__dispatch_group_registration_packet()
                elif choice == "3":
                    self.__dispatch_group_broadcast_packet()
                elif choice == "4":
                    self.__dispatch_status_story_packet()
                elif choice == "5":
                    # Requests centralized cache list parameters from the active hub socket
                    self.client_socket.send(json.dumps({"action": "VIEW_STATUS"}).encode('utf-8'))
                    time.sleep(1.0) # Grace period allowance frame for console output processing
                elif choice == "6":
                    self.trigger_media_call_handshake(call_type="AUDIO")
                elif choice == "7":
                    self.trigger_media_call_handshake(call_type="VIDEO")
                elif choice == "8":
                    print("\n[ Graceful Disconnect ]: Terminating active device registry allocations.")
                    self.is_connected = False
                    self.client_socket.close()
                    break
                else:
                    print("[INVALID CHOICE]: Select valid numeric indices from the menu tracker.")
            except Exception:
                print("[ERROR]: Interface dashboard component encountered execution drops.")
                break

    def __dispatch_private_message_packet(self) -> None:
        """
        Ingests user payload text arrays and pipes them securely to destination user handles.
        """
        target_peer = input("Enter destination username node: ").strip().upper()
        if not target_peer:
            return
        msg_body = input(f"Type private chat text to {target_peer}: ").strip()
        if not msg_body:
            return

        packet = json.dumps({
            "action": "PRIVATE_MSG",
            "target": target_peer,
            "msg": msg_body
        })
        try:
            self.client_socket.send(packet.encode('utf-8'))
            print(f"[SENT DM]: Outbound payload routed successfully to node: {target_peer}")
        except Exception:
            print("[ERROR]: Failed routing private messaging frame.")

    def __dispatch_group_registration_packet(self) -> None:
        """
        Compiles bounded arrays to register multi-user conversational domains.
        """
        group_id = input("Enter new WhatsApp group name token: ").strip().upper()
        if not group_id:
            return
        
        print("Enter group member usernames sequentially [Type 'DONE' to finalize lists]:")
        member_list = []
        while True:
            member_node = input("  Add Member: ").strip().upper()
            if member_node == "DONE":
                break
            if member_node:
                member_list.append(member_node)

        packet = json.dumps({
            "action": "CREATE_GROUP",
            "group_name": group_id,
            "members": member_list
        })
        try:
            self.client_socket.send(packet.encode('utf-8'))
            print(f"[SYSTEM]: Group registry transaction context fired for domain: {group_id}")
        except Exception:
            print("[ERROR]: Group provisioning drop error.")

    def __dispatch_group_broadcast_packet(self) -> None:
        """
        Pipes direct broadcast text payloads to target multi-user registries.
        """
        group_id = input("Enter target group domain token: ").strip().upper()
        if not group_id:
            return
        msg_body = input(f"Type broadcast message to group {group_id}: ").strip()
        if not msg_body:
            return

        packet = json.dumps({
            "action": "GROUP_MSG",
            "group_name": group_id,
            "msg": msg_body
        })
        try:
            self.client_socket.send(packet.encode('utf-8'))
            print(f"[SENT BROADCAST]: Payload injected inside group: {group_id}")
        except Exception:
            print("[ERROR]: Failed broadcasting group communication packet.")

    def __dispatch_status_story_packet(self) -> None:
        """
        Ingests temporary story vectors targeting global distribution frameworks.
        """
        status_body = input("Type your 24-hour status story text here: ").strip()
        if not status_body:
            return

        packet = json.dumps({
            "action": "POST_STATUS",
            "msg": status_body
        })
        try:
            self.client_socket.send(packet.encode('utf-8'))
            print("[SUCCESS]: Active text story uploaded to the central storage networks.")
        except Exception:
            print("[ERROR]: Status story pipeline submission error.")
    def __simulate_console_media_stream(self, room_id: str, call_type: str, direction_label: str) -> None:
        """
        Simulates peripheral audio/video network package streams over console interfaces.
        Enforces tight blocking loops for 10 sequential clocks to mock active connection sessions.
        """
        print(f"\n" + "*" * 60)
        print(f"  ⚡ CONNECTING REAL-TIME MEDIA CONFERENCING PERIPHERALS ⚡")
        print(f"  * ALLOCATION ROOM ID : {room_id}")
        print(f"  * STREAM FORMAT TYPE : {call_type} LINE ROUTE")
        print(f"  * SESSION DIRECTION  : {direction_label}")
        print("*" * 60)
        
        # Simulates 10 dynamic payload buffer transfers line by line securely
        for seconds in range(1, 11):
            sys.stdout.write(
                f"\r  [ ACTIVE CALL ROOM: {room_id} ] Pumping {call_type} packets... Frame #{seconds:02d}/10"
            )
            sys.stdout.flush()
            time.sleep(1) # Replicates standard 1 second media decay step latency parameters
            
        print(f"\n\n[ CALL DISCONNECTED ]: Conference room session reference {room_id} terminated gracefully.")
        print("=" * 60 + "\n")


# =====================================================================
# 7. CENTRAL RUNTIME APPLICATION CLIENT ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    # Instantiates a fresh independent client session node targeting the local host address
    whatsapp_messenger = WhatsAppClient(server_host="127.0.0.1", server_port=9999)
    
    # Boots up user identification and logs user into active server registries
    whatsapp_messenger.initialize_session()
