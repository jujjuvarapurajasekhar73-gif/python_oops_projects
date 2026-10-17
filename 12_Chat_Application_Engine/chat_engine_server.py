import socket
import threading
import time
import json
import sys

# =====================================================================
# 1. ENTERPRISE REGISTERED CANDIDATE SECURITY REGISTRY
# =====================================================================

class WhatsAppUserRegistry:
    def __init__(self) -> None:
        """
        Initializes hardcoded validated credential matrices.
        Acts as the central account database repository layer.
        """
        # Encodes primary user pairs directly to establish network client validation maps
        self.valid_accounts = {
            "MAMA": "MAMA_123",
            "RAJA": "RAJA_123",
            "CHINNI": "CHINNI_123",
            "SURESH": "SURESH_123"
        }

    def authenticate(self, username: str, token: str) -> bool:
        """
        Validates the incoming token payload against the secure registered storage.
        """
        user_key = username.strip().upper()
        return user_key in self.valid_accounts and self.valid_accounts[user_key] == token


# =====================================================================
# 2. CENTRAL ADVANCED WHATSAPP HUB SERVER ENGINE
# =====================================================================

class WhatsAppCentralServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 9999) -> None:
        """
        Initializes the central core router configuration arrays.
        Manages live socket descriptors, dynamic group lists, and offline buffers.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.auth_db = WhatsAppUserRegistry()
        
        # Isolated runtime registers managed through secure resource locking mappings
        self.active_connections = {}  # Format: {USERNAME: socket_object}
        self.offline_messages = {}    # Format: {USERNAME: [list of cached JSON string objects]}
        self.group_registry = {}      # Format: {GROUP_NAME: [list of member username strings]}
        self.status_stories = {}       # Format: {USERNAME: {"text": payload, "timestamp": epoch_float}}
        
        self.lock = threading.Lock()

    def boot_server(self) -> None:
        """
        Binds the network socket descriptor and spawns the listener loop thread tracker.
        """
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            print(f">>> CENTRAL WHATSAPP ENGINE ONLINE: LISTENING ON {self.host}:{self.port} <<<")
            
            # Starts the background story janitor thread loop tracker immediately
            threading.Thread(target=self.__cleanup_expired_statuses, daemon=True).start()
            
            self.__accept_connections_loop()
        except Exception as e:
            print(f"[CRITICAL BOOT ERROR]: System failed initialization: {e}")
            sys.exit(1)

    def __accept_connections_loop(self) -> None:
        """
        Continuous inbound client registration listener execution loop frame.
        """
        while True:
            try:
                client_socket, client_address = self.server_socket.accept()
                # Spawns a dedicated tracking thread for each raw incoming socket connection node
                threading.Thread(target=self.__handle_client_handshake, args=(client_socket,), daemon=True).start()
            except Exception:
                break
    def __handle_client_handshake(self, client_socket: socket.socket) -> None:
        """
        Executes strict protocol verification checking before creating active user memory locks.
        """
        try:
            # Captures authentication payload securely from raw connection stream
            handshake_payload = client_socket.recv(4096).decode('utf-8')
            if not handshake_payload:
                client_socket.close()
                return

            auth_data = json.loads(handshake_payload)
            username = auth_data.get("username", "").strip().upper()
            token = auth_data.get("token", "")

            # Authentication Verification Core Gate Entry
            if self.auth_db.authenticate(username, token):
                with self.lock:
                    # Enforces unique device constraint rules by booting active instances
                    if username in self.active_connections:
                        try:
                            old_sock = self.active_connections[username]
                            old_sock.send(json.dumps({"action": "ALERT", "msg": "Logged in from another device."}).encode('utf-8'))
                            old_sock.close()
                        except Exception:
                            pass
                    
                    self.active_connections[username] = client_socket
                
                print(f"[ONLINE]: Account validated successfully: {username}")
                client_socket.send(json.dumps({"status": "SUCCESS", "msg": "Authenticated."}).encode('utf-8'))
                
                # Dynamic Offline Messages Flushing Mechanism
                self.__flush_cached_offline_messages(username, client_socket)
                
                # Registers active messaging listener row pipeline for the lifecycle session
                self.__client_messaging_runtime(username, client_socket)
            else:
                client_socket.send(json.dumps({"status": "FAILED", "msg": "Invalid credentials."}).encode('utf-8'))
                client_socket.close()
        except Exception as e:
            try:
                client_socket.close()
            except Exception:
                pass

    def __flush_cached_offline_messages(self, username: str, client_socket: socket.socket) -> None:
        """
        Pipes all stored offline buffer packets directly onto newly established active descriptors.
        """
        with self.lock:
            if username in self.offline_messages and self.offline_messages[username]:
                print(f"[BUFFER FLUSH]: Pumping pending cached packets into account: {username}")
                for msg_packet in self.offline_messages[username]:
                    try:
                        client_socket.send(msg_packet.encode('utf-8'))
                        time.sleep(0.1) # Tiny structural network pacing decay step
                    except Exception:
                        break
                # Flushes the tracking reference list completely upon validation
                self.offline_messages[username] = []

    def __client_messaging_runtime(self, username: str, client_socket: socket.socket) -> None:
        """
        Main continuous event processor tracking active packet ingestion frames per client.
        """
        while True:
            try:
                raw_packet = client_socket.recv(4096).decode('utf-8')
                if not raw_packet:
                    break

                packet_data = json.loads(raw_packet)
                action = packet_data.get("action", "")

                if action == "PRIVATE_MSG":
                    self.__route_private_message(username, packet_data)
                elif action == "CREATE_GROUP":
                    self.__register_new_group(username, packet_data)
                elif action == "GROUP_MSG":
                    self.__broadcast_group_message(username, packet_data)
                elif action == "POST_STATUS":
                    self.__ingest_status_story(username, packet_data)
                elif action == "VIEW_STATUS":
                    self.__dispatch_active_statuses(client_socket)
                elif action == "INIT_CALL":
                    self.__establish_call_handshake(username, packet_data)

            except Exception:
                break

        # Session Demolition Module Row Execution
        self.__demolish_client_session(username)

    def __route_private_message(self, sender: str, packet: dict) -> None:
        """
        Routes point-to-point text streams or buffers the payload if the destination is dead.
        """
        target = packet.get("target", "").strip().upper()
        message_payload = packet.get("msg", "")
        
        outgoing_packet = json.dumps({
            "action": "RECEIVE_PRIVATE",
            "sender": sender,
            "msg": message_payload,
            "timestamp": time.strftime('%H:%M:%S')
        })

        with self.lock:
            if target in self.active_connections:
                try:
                    self.active_connections[target].send(outgoing_packet.encode('utf-8'))
                    print(f"[ROUTED]: {sender} -> {target} (Direct Delivery)")
                except Exception:
                    self.__cache_offline_packet(target, outgoing_packet)
            else:
                self.__cache_offline_packet(target, outgoing_packet)

    def __cache_offline_packet(self, target: str, packet_string: str) -> None:
        """
        Internal Memory allocation sub-routine safeguarding transaction values.
        """
        if target not in self.offline_messages:
            self.offline_messages[target] = []
        self.offline_messages[target].append(packet_string)
        print(f"[BUFFERED]: Destination {target} unreachable. Packet cached in buffer storage.")

    def __register_new_group(self, creator: str, packet: dict) -> None:
        """
        Allocates isolated shared broadcast domains with bounded access list structures.
        """
        group_name = packet.get("group_name", "").strip().upper()
        members = packet.get("members", []) # Expects tracking list of standard uppercase user handles
        
        # Injects the active creator signature implicitly inside the target domain configuration
        cleaned_members = [m.strip().upper() for m in members]
        if creator not in cleaned_members:
            cleaned_members.append(creator)

        with self.lock:
            self.group_registry[group_name] = cleaned_members
            print(f"[GROUP REGISTERED]: Domain {group_name} built successfully with members {cleaned_members}")
            
            # Notifies all active target units about the new domain layout mapping parameters
            notification = json.dumps({"action": "ALERT", "msg": f"You were added to group: {group_name}"})
            for member in cleaned_members:
                if member in self.active_connections and member != creator:
                    try:
                        self.active_connections[member].send(notification.encode('utf-8'))
                    except Exception:
                        pass

    def __broadcast_group_message(self, sender: str, packet: dict) -> None:
        """
        Pipes broad transmission arrays inside specific access boundaries sequentially.
        """
        group_name = packet.get("group_name", "").strip().upper()
        message_payload = packet.get("msg", "")

        outgoing_packet = json.dumps({
            "action": "RECEIVE_GROUP",
            "group": group_name,
            "sender": sender,
            "msg": message_payload,
            "timestamp": time.strftime('%H:%M:%S')
        })

        with self.lock:
            if group_name not in self.group_registry:
                return
            
            target_list = self.group_registry[group_name]
            if sender not in target_list:
                return # Security check constraint rule: Rejects cross-domain intrusions

            for target in target_list:
                if target != sender:
                    if target in self.active_connections:
                        try:
                            self.active_connections[target].send(outgoing_packet.encode('utf-8'))
                        except Exception:
                            self.__cache_offline_packet(target, outgoing_packet)
                    else:
                        self.__cache_offline_packet(target, outgoing_packet)
            print(f"[BROADCAST]: Message from {sender} mirrored inside group {group_name}")
    def __ingest_status_story(self, username: str, packet: dict) -> None:
        """
        Registers a new status story linked to a temporary timestamp array.
        Enforces strict 24-hour expiration boundaries globally.
        """
        status_text = packet.get("msg", "").strip()
        
        with self.lock:
            self.status_stories[username] = {
                "text": status_text,
                "timestamp": time.time()
            }
            print(f"[STATUS POSTED]: {username} uploaded text story: '{status_text}'")
            
        notification = json.dumps({"action": "ALERT", "msg": f"{username} updated their active status story."})
        self.__broadcast_global_system_alert(notification, exclude_user=username)

    def __dispatch_active_statuses(self, client_socket: socket.socket) -> None:
        """
        Compiles and streams all valid active status stories back to the requesting client descriptor.
        """
        status_view_map = {}
        with self.lock:
            current_epoch = time.time()
            for user, data in self.status_stories.items():
                # Enforces 24-hour verification block inside display pipelines as well (86400 seconds)
                if current_epoch - data["timestamp"] < 86400:
                    status_view_map[user] = data["text"]

        outgoing_packet = json.dumps({
            "action": "STATUS_LIST",
            "data": status_view_map
        })
        try:
            client_socket.send(outgoing_packet.encode('utf-8'))
        except Exception:
            pass

    def __cleanup_expired_statuses(self) -> None:
        """
        Asynchronous Background Janitor Thread Loop: Runs non-stop to evaluate structural timestamps.
        """
        while True:
            time.sleep(10) # Evaluates the register cycles sequentially every 10 seconds standard rest pacing
            with self.lock:
                current_epoch = time.time()
                expired_users = []
                for user, data in self.status_stories.items():
                    # 86400 seconds standard frame = 24 Hours absolute limit threshold
                    if current_epoch - data["timestamp"] >= 86400:
                        expired_users.append(user)
                
                for user in expired_users:
                    del self.status_stories[user]
                    print(f"[JANITOR CLEANUP]: Expired status story removed automatically for account: {user}")

    def __establish_call_handshake(self, sender: str, packet: dict) -> None:
        """
        Routes initialization negotiation profiles to bind peer audio/video pipeline sessions.
        """
        target = packet.get("target", "").strip().upper()
        call_type = packet.get("call_type", "VIDEO") # Supports strict AUDIO / VIDEO configurations
        room_id = packet.get("room_id", "")

        forward_packet = json.dumps({
            "action": "INBOUND_CALL",
            "sender": sender,
            "call_type": call_type,
            "room_id": room_id
        })

        with self.lock:
            if target in self.active_connections:
                try:
                    self.active_connections[target].send(forward_packet.encode('utf-8'))
                    print(f"[CALL HANDSHAKE]: Routing {call_type} connection request from {sender} -> {target}")
                except Exception:
                    self.__notify_call_failure(sender, target, "Destination reference disconnected unexpectedly.")
            else:
                self.__notify_call_failure(sender, target, "User is currently offline.")

    def __notify_call_failure(self, sender: str, target: str, reason: str) -> None:
        """
        Alerts origin nodes instantly if peer descriptor endpoints break down mid-handshake.
        """
        fail_packet = json.dumps({
            "action": "ALERT",
            "msg": f"Cannot connect call to {target}. Reason: {reason}"
        })
        if sender in self.active_connections:
            try:
                self.active_connections[sender].send(fail_packet.encode('utf-8'))
            except Exception:
                pass

    def __broadcast_global_system_alert(self, notification_string: str, exclude_user: str) -> None:
        """
        Internal global transport module broadcasting event metrics to all live connected endpoints.
        """
        with self.lock:
            for user, sock in self.active_connections.items():
                if user != exclude_user:
                    try:
                        sock.send(notification_string.encode('utf-8'))
                    except Exception:
                        pass

    def __demolish_client_session(self, username: str) -> None:
        """
        Handles graceful resource decomposition constraints whenever user connection hits dead flags.
        """
        with self.lock:
            if username in self.active_connections:
                try:
                    self.active_connections[username].close()
                except Exception:
                    pass
                del self.active_connections[username]
                print(f"[OFFLINE]: Inbound session closed down for user node: {username}")
# =====================================================================
# 7. CENTRAL RUNTIME APPLICATION SYSTEM ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    # Creates the standalone server deployment instance targeting the default infrastructure port
    whatsapp_hub = WhatsAppCentralServer(host="127.0.0.1", port=9999)
    
    # Boots up the core engine listener framework arrays
    whatsapp_hub.boot_server()
