//
//  SignupData.swift
//  SideEffects
//
//  Created by Kevin Tran on 11/1/19.
//  Copyright © 2019 Kevin Tran. All rights reserved.
//

import Combine
import SwiftUI

final class SignupData: ObservableObject {
    @Published var username = ""
    @Published var password = ""
    @Published var firstname = ""
    @Published var lastname = ""
    @Published var email = ""
    
    func validate() -> Bool {
        if username == "" || password == "" ||
           firstname == "" || lastname == "" ||
           email == "" { return false }
        return true
    }

    func create_keys_values() -> String {
        return "?username=" + username +
               "&password=" + password +
               "&first_name=" + firstname +
               "&last_name=" + lastname +
               "&email=" + email
    }
}
