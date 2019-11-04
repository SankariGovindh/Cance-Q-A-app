//
//  LoginData.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/1/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import SwiftUI

final class LoginData: ObservableObject  {
    @Published var username = ""
    @Published var password = ""
    
    func validate() -> Bool {
        if username == "" || password == "" { return false }
        return true
    }
    
    func create_keys_values() -> String {
        return "?username=" + username +
               "&password=" + password
    }
}
